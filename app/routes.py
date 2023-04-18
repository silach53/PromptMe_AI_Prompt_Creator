from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from app import db
from app.models import Prompt, Block
from app.forms import CreatePromptForm, EditPromptForm
import requests
import json

main = Blueprint("main", __name__)

@main.route("/")
def index():
    prompts = Prompt.query.all()
    return render_template("index.html", prompts=prompts)

@main.route("/create_prompt", methods=["GET", "POST"])
def create_prompt():
    form = CreatePromptForm()
    if form.validate_on_submit():
        prompt = Prompt(title=form.title.data)
        db.session.add(prompt)
        db.session.commit()

        for block in form.blocks.data:
            with open('block.txt','w') as f:
                f.write(json.dumps(block))
            block_instance = Block(prompt_id=prompt.id, block_type=block["block_type"], content=block["content"], order=block["order"])
            db.session.add(block_instance)
        db.session.commit()

        flash("Prompt created successfully.", "success")
        return redirect(url_for("main.index"))

    return render_template("create_prompt.html", form=form)

@main.route("/edit_prompt/<int:prompt_id>", methods=["GET", "POST"])
def edit_prompt(prompt_id):
    prompt = Prompt.query.get_or_404(prompt_id)
    form = EditPromptForm(obj=prompt)

    if form.validate_on_submit():
        prompt.title = form.title.data
        db.session.commit()

        for block_data in form.blocks.data:
            block = Block.query.get(block_data["id"])
            if block:
                block.block_type = block_data["block_type"]
                block.content = block_data["content"]
                block.order = block_data["order"]
            else:
                new_block = Block(prompt_id=prompt.id, block_type=block_data["block_type"], content=block_data["content"], order=block_data["order"])
                db.session.add(new_block)
        db.session.commit()

        flash("Prompt updated successfully.", "success")
        return redirect(url_for("main.view_prompt", prompt_id=prompt_id))

    form.blocks.entries = [{"id": block.id, "block_type": block.block_type, "content": block.content, "order": block.order} for block in prompt.blocks]

    return render_template("edit_prompt.html", form=form, prompt_id=prompt_id)

@main.route("/view_prompt/<int:prompt_id>")
def view_prompt(prompt_id):
    prompt = Prompt.query.get_or_404(prompt_id)
    return render_template("view_prompt.html", prompt=prompt)

@main.route("/generate_ai_response/<int:prompt_id>", methods=["POST"])
def generate_ai_response(prompt_id):
    prompt = Prompt.query.get_or_404(prompt_id)
    prompt_text = "\n".join([block.content for block in prompt.blocks])

    # Replace with the actual API call to ChatGPT
    response = requests.post("https://api.openai.com/v1/engines/davinci-codex/completions", json={"prompt": prompt_text})

    if response.status_code == 200:
        generated_text = response.json()["choices"][0]["text"]
        prompt.ai_response = generated_text
        db.session.commit()
        return jsonify({"response": generated_text})
    else:
        return jsonify({"error": "Failed to generate AI response."}), 500

@main.route("/copy_result/<int:prompt_id>", methods=["GET"])
def copy_result(prompt_id):
    prompt = Prompt.query.get_or_404(prompt_id)
    return jsonify({"result": prompt.ai_response})
