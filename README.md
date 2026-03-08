# FastAPI CRUD with PostgreSQL

Simple learning project for CRUD operations using:
- FastAPI
- SQLAlchemy ORM
- PostgreSQL

## 1. Create database

Make sure PostgreSQL is running, then create a database:

```sql
CREATE DATABASE fastapi_crud;
```

Default connection used in the project:

`postgresql+psycopg2://postgres:postgres@localhost:5432/fastapi_crud`

If your username/password is different, edit `app/database.py`.

## 2. Install dependencies

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 3. Run server

```bash
uvicorn app.main:app --reload
```

Open docs:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 4. CRUD endpoints

- `POST /items` create item
- `GET /items` list items
- `GET /items/{item_id}` get one item
- `PUT /items/{item_id}` update item
- `DELETE /items/{item_id}` delete item
