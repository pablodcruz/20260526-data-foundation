import csv
import re
from datetime import datetime

from config import PostgresConfig
from database import (
    clear_staging,
    get_connection,
    init_db,
    insert_staging_customers,
    list_customers,
    promote_staging_to_customers,
)

INPUT_CSV = "data/fake_customers.csv"

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def extract_csv(file_path):
    with open(file_path, "r", encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def parse_boolean(value):
    return str(value).strip().lower() in {"true", "1", "yes", "y", "t"}


def parse_date(value):
    value = value.strip()
    if not value:
        return None
    for fmt in ("%Y-%m-%d", "%m/%d/%Y", "%d-%m-%Y"):
        try:
            return datetime.strptime(value, fmt).date()
        except ValueError:
            continue
    raise ValueError(f"Invalid date format: {value}")


def valid_email(email):
    return bool(EMAIL_RE.match(email.strip()))


def transform_row(row):
    first_name = row.get("first_name", "").strip().title()
    last_name = row.get("last_name", "").strip().title()
    email = row.get("email", "").strip().lower()
    country = row.get("country", "").strip().title() or None
    notes = row.get("notes", "").strip() or None

    if not first_name or not last_name or not email or not valid_email(email):
        return None

    signup_date = parse_date(row.get("signup_date", "")) if row.get("signup_date") else None

    return {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "country": country,
        "signup_date": signup_date,
        "is_active": parse_boolean(row.get("is_active", "true")),
        "notes": notes,
    }


def transform_rows(rows):
    cleaned = []
    rejected = []
    for row in rows:
        try:
            transformed = transform_row(row)
        except ValueError as exc:
            rejected.append({**row, "error": str(exc)})
            continue
        if transformed is None:
            rejected.append({**row, "error": "Missing required fields or invalid email"})
            continue
        cleaned.append(transformed)
    return cleaned, rejected


def load_rows(rows, config):
    with get_connection(config) as connection:
        init_db(connection)
        insert_staging_customers(connection, rows)
        promote_staging_to_customers(connection)
        clear_staging(connection)
        return list_customers(connection, limit=10)


def main():
    raw_rows = extract_csv(INPUT_CSV)
    cleaned_rows, rejected_rows = transform_rows(raw_rows)

    print(f"Extracted rows: {len(raw_rows)}")
    print(f"Cleaned rows: {len(cleaned_rows)}")
    print(f"Rejected rows: {len(rejected_rows)}")

    if rejected_rows:
        print("Rejected rows preview:")
        for row in rejected_rows[:3]:
            print(row)

    config = PostgresConfig()
    customers = load_rows(cleaned_rows, config)

    print("Loaded customers preview:")
    for customer in customers:
        print(customer)


if __name__ == "__main__":
    main()
