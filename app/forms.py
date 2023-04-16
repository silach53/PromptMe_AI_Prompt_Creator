from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField, FormField, FieldList
from wtforms.validators import DataRequired, Optional

class BlockForm(FlaskForm):
    block_id = StringField("ID", validators=[Optional()])
    block_type = SelectField("Block Type", choices=[("instruction", "Model Instruction"), ("task", "Task Text"), ("comment", "Additional Comments"), ("code", "Code")], validators=[DataRequired()])
    content = TextAreaField("Content", validators=[DataRequired()])
    order = StringField("Order", validators=[DataRequired()])

class CreatePromptForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    blocks = FieldList(FormField(BlockForm), min_entries=1)
    submit = SubmitField("Create Prompt")

class EditPromptForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    blocks = FieldList(FormField(BlockForm), min_entries=1)
    submit = SubmitField("Update Prompt")
