from flask import Blueprint, jsonify, request

from service.todo_service import (
    create_todo,
    delete_todo,
    get_all_todos,
    get_todo_by_id,
    update_todo,
)


todo_blueprint = Blueprint("todos", __name__, url_prefix="/todos")


@todo_blueprint.get("")
def list_todos():
    todos = get_all_todos()
    return jsonify([todo.to_dict() for todo in todos]), 200


@todo_blueprint.get("/<int:todo_id>")
def retrieve_todo(todo_id):
    todo = get_todo_by_id(todo_id)

    if todo is None:
        return jsonify({"error": "Todo not found"}), 404

    return jsonify(todo.to_dict()), 200


@todo_blueprint.post("")
def add_todo():
    data = request.get_json(silent=True) or {}
    todo, error = create_todo(data)

    if error:
        return jsonify({"error": error}), 400

    return jsonify(todo.to_dict()), 201


@todo_blueprint.put("/<int:todo_id>")
def edit_todo(todo_id):
    data = request.get_json(silent=True) or {}
    todo, error = update_todo(todo_id, data)

    if error == "Todo not found":
        return jsonify({"error": error}), 404

    if error:
        return jsonify({"error": error}), 400

    return jsonify(todo.to_dict()), 200


@todo_blueprint.delete("/<int:todo_id>")
def remove_todo(todo_id):
    deleted = delete_todo(todo_id)

    if not deleted:
        return jsonify({"error": "Todo not found"}), 404

    return jsonify({"message": "Todo deleted"}), 200

