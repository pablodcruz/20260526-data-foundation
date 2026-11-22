import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from app import create_app
from database import todo_database


class TestTodoApi(unittest.TestCase):
    def test_todo_lifecycle(self):
        with TemporaryDirectory() as temp_dir:
            db_path = Path(temp_dir) / "test.db"
            with patch.object(todo_database, "DB_PATH", db_path):
                app = create_app()
                app.config["TESTING"] = True
                with app.test_client() as client:
                    self.assertEqual(client.get("/todos").get_json(), [])

                    created = client.post("/todos", json={"title": "Study Flask"})
                    self.assertEqual(created.status_code, 201)
                    todo = created.get_json()
                    self.assertEqual(todo["title"], "Study Flask")
                    self.assertFalse(todo["completed"])
                    url = f"/todos/{todo['id']}"
                    self.assertEqual(client.get(url).get_json(), todo)

                    updated = client.put(url, json={"completed": True})
                    self.assertEqual(updated.status_code, 200)
                    self.assertTrue(updated.get_json()["completed"])
                    self.assertTrue(client.get(url).get_json()["completed"])

                    self.assertEqual(client.delete(url).status_code, 200)
                    self.assertEqual(client.get(url).status_code, 404)
                    self.assertEqual(client.get("/todos").get_json(), [])
