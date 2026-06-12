import pandas as pd
import psycopg2


DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "etl_demo",
    "user": "postgres",
    "password": "postgres",
}


def get_connection():
    return psycopg2.connect(**DB_CONFIG)


def create_table():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                DROP TABLE IF EXISTS customers;

                CREATE TABLE customers (
                    customer_id INTEGER,
                    first_name VARCHAR(50),
                    last_name VARCHAR(50),
                    email VARCHAR(100),
                    purchase_amount NUMERIC(10, 2)
                );
            """)


def load_from_dataframe(df):
    records = df.to_records(index=False)

    with get_connection() as conn:
        with conn.cursor() as cur:
            for row in records:
                cur.execute("""
                    INSERT INTO customers
                    VALUES (%s, %s, %s, %s, %s);
                """, tuple(row))


def load_from_dict(data_dict):
    df = pd.DataFrame(data_dict)
    load_from_dataframe(df)


def load_from_list(data_list):
    df = pd.DataFrame(
        data_list,
        columns=["customer_id", "first_name", "last_name", "email", "purchase_amount"]
    )
    load_from_dataframe(df)


def load_from_tuple(data_tuple):
    df = pd.DataFrame(
        list(data_tuple),
        columns=["customer_id", "first_name", "last_name", "email", "purchase_amount"]
    )
    load_from_dataframe(df)


def main():
    create_table()

    # Starting data as a DataFrame
    df = pd.DataFrame({
        "customer_id": [1, 2],
        "first_name": ["Pablo", "Ana"],
        "last_name": ["Cruz", "Santos"],
        "email": ["pablo@email.com", "ana@email.com"],
        "purchase_amount": [120.50, 75.00],
    })

    load_from_dataframe(df)

    data_dict = {
        "customer_id": [3],
        "first_name": ["Jose"],
        "last_name": ["Perez"],
        "email": ["jose@email.com"],
        "purchase_amount": [300.25],
    }

    load_from_dict(data_dict)

    data_list = [
        [4, "Maria", "Lopez", "maria@email.com", 50.00],
    ]

    load_from_list(data_list)

    data_tuple = (
        (5, "Luis", "Diaz", "luis@email.com", 90.00),
    )

    load_from_tuple(data_tuple)

    print("Data loaded into PostgreSQL.")


if __name__ == "__main__":
    main()