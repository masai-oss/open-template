from app.main import db
from app.main.models.todo import Todo
from flask import jsonify


def add_new_todo(data):
    todo = Todo(
        todo_item=data['todo']
    )
    save_changes(todo)
    response_object = jsonify({"response": "successfully added todo"})
    return response_object, 200


def save_changes(data):
    db.session.add(data)
    db.session.commit()
