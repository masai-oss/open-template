from .. import db


class Todo(db.Model):
    __tablename__ = 'todo'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    todo_item = db.Column(db.String(250), nullable=False)
