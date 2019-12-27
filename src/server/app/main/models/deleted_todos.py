from .. import db


class RemovedTodo(db.Model):
    __tablename__ = 'removed_todos'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    todo_item = db.Column(db.String(250), nullable=False)