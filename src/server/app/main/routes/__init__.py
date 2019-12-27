from .blueprint_todo import todo


def register_blueprints(app):
    app.register_blueprint(todo, url_prefix="/todo")
