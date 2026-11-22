# Todo API

A simple Flask CRUD API with three layers:

- `controllers/`: HTTP routes and responses
- `service/`: validation and business logic
- `database/`: SQLite database access
- `models/`: Python objects used by the app

## Setup

From this demo directory (`demos/todo-api`), create and activate a virtual environment.
On macOS or Linux:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows PowerShell, activate with `.\.venv\Scripts\Activate.ps1` instead.
Flask is the only direct dependency; SQLite is included with Python.

## Test

```bash
python -m unittest discover -s test -v
```

The API test uses a temporary SQLite database and does not start a web server.

## Run

```bash
python app.py
```

The API runs at:

```text
http://127.0.0.1:5000
```

## Endpoints

```text
GET    /todos
GET    /todos/<id>
POST   /todos
PUT    /todos/<id>
DELETE /todos/<id>
```

## Example Requests

Create a todo:

```bash
curl -X POST http://127.0.0.1:5000/todos \
  -H "Content-Type: application/json" \
  -d "{\"title\":\"Study Flask\",\"description\":\"Practice CRUD routes\"}"
```

Update a todo:

```bash
curl -X PUT http://127.0.0.1:5000/todos/1 \
  -H "Content-Type: application/json" \
  -d "{\"title\":\"Study Flask\",\"description\":\"Practice layers\",\"completed\":true}"
```
