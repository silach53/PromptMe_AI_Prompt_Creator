if __name__ == '__main__':
    from __init__ import db
else:
    from app import db
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    prompts = db.relationship("Prompt", backref="user", lazy=True)

class Prompt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)
    blocks = db.relationship("Block", backref="prompt", lazy=True, order_by="Block.order")
    ai_response = db.Column(db.Text, nullable=True)

class Block(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prompt_id = db.Column(db.Integer, db.ForeignKey("prompt.id"), nullable=False)
    block_type = db.Column(db.String(64), nullable=False)
    content = db.Column(db.Text, nullable=False)
    order = db.Column(db.Integer, nullable=False)



'''Короче странно, если хочу запустить этой файл, то выдаст ошибку потому что модуля app не существует
Если поменять на __init__ то бд создасться и после этого уже из run.py import app здесь работает'''
def main():
    USERNAME = "workalexandr"  # замените на свой логин
    connection_string = f"postgresql+psycopg2://{USERNAME}:@localhost:5433/{USERNAME}"
    engine = create_engine(connection_string)
    db.metadata.create_all(engine)

if __name__ == '__main__':
    main()