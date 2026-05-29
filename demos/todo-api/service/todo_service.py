from database.todo_database import (
    create_todo_record,
    delete_todo_record,
    fetch_all_todos,
    fetch_todo_by_id,
    update_todo_record,
)


def get_all_todos():
    return fetch_all_todos()


def get_todo_by_id(todo_id):
    return fetch_todo_by_id(todo_id)


def create_todo(data):
    title = data.get("title", "")
    description = data.get("description", "")

    if not isinstance(title, str):
        return None, "Title must be text"

    if not isinstance(description, str):
        return None, "Description must be text"

    title = title.strip()
    description = description.strip()

    if not title:
        return None, "Title is required"

    todo = create_todo_record(title, description)
    return todo, None


def update_todo(todo_id, data):
    existing_todo = fetch_todo_by_id(todo_id)

    if existing_todo is None:
        return None, "Todo not found"

    title = data.get("title", existing_todo.title)
    description = data.get("description", existing_todo.description)
    completed = data.get("completed", existing_todo.completed)

    if not isinstance(title, str):
        return None, "Title must be text"

    if not isinstance(description, str):
        return None, "Description must be text"

    title = title.strip()
    description = description.strip()

    if not title:
        return None, "Title is required"

    if not isinstance(completed, bool):
        return None, "Completed must be true or false"

    todo = update_todo_record(todo_id, title, description, completed)
    return todo, None


def delete_todo(todo_id):
    return delete_todo_record(todo_id)
