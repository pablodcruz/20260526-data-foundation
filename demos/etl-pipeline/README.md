# ETL Pipeline Demo

A simple ETL demo that reads fake customer data from a CSV file, cleans it, and loads it into a PostgreSQL database using plain `psycopg2` SQL.

## What it includes

- `etl.py`: extract-transform-load pipeline
- `database.py`: PostgreSQL connection and CRUD methods without SQLAlchemy
- `config.py`: database connection configuration via environment variables
- `data/fake_customers.csv`: sample fake customer dataset

## Setup

1. Create a Postgres database and user.

2. Install dependencies:

```bash
cd demos/etl-pipeline
pip install -r requirements.txt
```

3. Set environment variables for your Postgres connection.

PowerShell / Windows CMD:

```powershell
$env:POSTGRES_HOST = 'localhost'
$env:POSTGRES_PORT = '5432'
$env:POSTGRES_DB = 'etl_demo'
$env:POSTGRES_USER = 'postgres'
$env:POSTGRES_PASSWORD = 'postgres'
```

macOS / Linux:

```bash
export POSTGRES_HOST=localhost
export POSTGRES_PORT=5432
export POSTGRES_DB=etl_demo
export POSTGRES_USER=postgres
export POSTGRES_PASSWORD=postgres
```

4. Run the ETL pipeline:

```bash
python etl.py
```

## Database schema

The demo creates two tables:

- `staging_customers` for raw CSV staging data
- `customers` for the cleaned production dataset

## CRUD methods

`database.py` includes:

- `create_customer`
- `get_customer`
- `list_customers`
- `update_customer`
- `delete_customer`

## Notes

- This demo uses plain SQL with `psycopg2`.
- It performs a Postgres `ON CONFLICT` upsert when moving staged rows into `customers`.
- No SQLAlchemy or ORM is used.
