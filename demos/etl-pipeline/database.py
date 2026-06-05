import psycopg2
from psycopg2.extras import RealDictCursor

from config import PostgresConfig


def get_connection(config: PostgresConfig = None):
    config = config or PostgresConfig()
    return psycopg2.connect(config.dsn())


def init_db(connection):
    with connection.cursor() as cursor:
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS staging_customers (
                staging_id SERIAL PRIMARY KEY,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT NOT NULL,
                country TEXT,
                signup_date DATE,
                is_active BOOLEAN,
                notes TEXT,
                created_at TIMESTAMPTZ DEFAULT NOW()
            )
            """
        )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS customers (
                customer_id SERIAL PRIMARY KEY,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                country TEXT,
                signup_date DATE,
                is_active BOOLEAN,
                notes TEXT,
                created_at TIMESTAMPTZ DEFAULT NOW(),
                updated_at TIMESTAMPTZ DEFAULT NOW()
            )
            """
        )
    connection.commit()


def insert_staging_customers(connection, rows):
    query = """
        INSERT INTO staging_customers (
            first_name, last_name, email, country, signup_date, is_active, notes
        ) VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    with connection.cursor() as cursor:
        cursor.executemany(
            query,
            [
                (
                    row["first_name"],
                    row["last_name"],
                    row["email"],
                    row["country"],
                    row["signup_date"],
                    row["is_active"],
                    row["notes"],
                )
                for row in rows
            ],
        )
    connection.commit()


def promote_staging_to_customers(connection):
    with connection.cursor() as cursor:
        cursor.execute(
            """
            INSERT INTO customers (
                first_name, last_name, email, country, signup_date, is_active, notes
            )
            SELECT first_name, last_name, email, country, signup_date, is_active, notes
            FROM staging_customers
            ON CONFLICT (email)
            DO UPDATE SET
                first_name = EXCLUDED.first_name,
                last_name = EXCLUDED.last_name,
                country = EXCLUDED.country,
                signup_date = EXCLUDED.signup_date,
                is_active = EXCLUDED.is_active,
                notes = EXCLUDED.notes,
                updated_at = NOW();
            """
        )
    connection.commit()


def clear_staging(connection):
    with connection.cursor() as cursor:
        cursor.execute("TRUNCATE staging_customers;")
    connection.commit()


def create_customer(connection, customer):
    query = """
        INSERT INTO customers (
            first_name, last_name, email, country, signup_date, is_active, notes
        ) VALUES (%s, %s, %s, %s, %s, %s, %s)
        RETURNING customer_id
    """
    with connection.cursor() as cursor:
        cursor.execute(
            query,
            (
                customer["first_name"],
                customer["last_name"],
                customer["email"],
                customer.get("country"),
                customer.get("signup_date"),
                customer.get("is_active", True),
                customer.get("notes"),
            ),
        )
        customer_id = cursor.fetchone()[0]
    connection.commit()
    return customer_id


def get_customer(connection, customer_id):
    query = "SELECT * FROM customers WHERE customer_id = %s"
    with connection.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute(query, (customer_id,))
        return cursor.fetchone()


def list_customers(connection, limit=100):
    query = "SELECT * FROM customers ORDER BY customer_id LIMIT %s"
    with connection.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute(query, (limit,))
        return cursor.fetchall()


def update_customer(connection, customer_id, fields):
    columns = []
    values = []
    for key, value in fields.items():
        columns.append(f"{key} = %s")
        values.append(value)
    if not columns:
        return False

    query = f"UPDATE customers SET {', '.join(columns)}, updated_at = NOW() WHERE customer_id = %s"
    values.append(customer_id)

    with connection.cursor() as cursor:
        cursor.execute(query, tuple(values))
        updated = cursor.rowcount > 0
    connection.commit()
    return updated


def delete_customer(connection, customer_id):
    query = "DELETE FROM customers WHERE customer_id = %s"
    with connection.cursor() as cursor:
        cursor.execute(query, (customer_id,))
        deleted = cursor.rowcount > 0
    connection.commit()
    return deleted
