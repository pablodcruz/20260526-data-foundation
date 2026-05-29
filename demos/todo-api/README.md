# Todo API

A simple Flask CRUD API with three layers:

- `controllers/`: HTTP routes and responses
- `service/`: validation and business logic
- `database/`: SQLite database access
- `models/`: Python objects used by the app

## Setup

```bash
pip install -r requirements.txt
```

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
