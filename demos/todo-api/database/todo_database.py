import sqlite3
from pathlib import Path

from models.todo import Todo


DB_PATH = Path(__file__).resolve().parent.parent / "todos.db"


def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def row_to_todo(row):
    if row is None:
        return None

    return Todo(
        id=row["id"],
        title=row["title"],
        description=row["description"],
        completed=bool(row["completed"]),
    )


def init_db():
    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS todos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL DEFAULT '',
                completed INTEGER NOT NULL DEFAULT 0
            )
            """
        )


def fetch_all_todos():
    with get_connection() as connection:
        rows = connection.execute(
            """
            SELECT id, title, description, completed
            FROM todos
            ORDER BY id
            """
        ).fetchall()

    return [row_to_todo(row) for row in rows]


def fetch_todo_by_id(todo_id):
    with get_connection() as connection:
        row = connection.execute(
            """
            SELECT id, title, description, completed
            FROM todos
            WHERE id = ?
            """,
            (todo_id,),
        ).fetchone()

    return row_to_todo(row)


def create_todo_record(title, description):
    with get_connection() as connection:
        cursor = connection.execute(
            """
            INSERT INTO todos (title, description)
            VALUES (?, ?)
            """,
            (title, description),
        )
        todo_id = cursor.lastrowid

    return fetch_todo_by_id(todo_id)


def update_todo_record(todo_id, title, description, completed):
    with get_connection() as connection:
        connection.execute(
            """
            UPDATE todos
            SET title = ?, description = ?, completed = ?
            WHERE id = ?
            """,
            (title, description, int(completed), todo_id),
        )

    return fetch_todo_by_id(todo_id)


def delete_todo_record(todo_id):
    with get_connection() as connection:
        cursor = connection.execute(
            """
            DELETE FROM todos
            WHERE id = ?
            """,
            (todo_id,),
        )

    return cursor.rowcount > 0
