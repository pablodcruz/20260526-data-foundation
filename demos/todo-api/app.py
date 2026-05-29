from flask import Flask

from controllers.todo_controller import todo_blueprint
from database.todo_database import init_db


def create_app():
    app = Flask(__name__)
    init_db()
    app.register_blueprint(todo_blueprint)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
