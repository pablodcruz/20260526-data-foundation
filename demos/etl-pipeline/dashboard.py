from collections import Counter, defaultdict
from pathlib import Path

import matplotlib.pyplot as plt
import streamlit as st

from config import PostgresConfig
from etl import extract_csv, transform_rows


BASE_DIR = Path(__file__).parent
DEFAULT_CSV = BASE_DIR / "data" / "fake_customers.csv"


st.set_page_config(page_title="ETL Pipeline Dashboard", layout="wide")


@st.cache_data
def load_pipeline_preview(csv_path):
    raw_rows = extract_csv(str(csv_path))
    cleaned_rows, rejected_rows = transform_rows(raw_rows)
    return raw_rows, cleaned_rows, rejected_rows


def load_database_customers(limit):
    from database import get_connection, init_db, list_customers

    config = PostgresConfig()
    with get_connection(config) as connection:
        init_db(connection)
        return list_customers(connection, limit=limit)


def load_cleaned_rows_to_database(rows):
    from etl import load_rows

    return load_rows(rows, PostgresConfig())


def count_by(rows, key):
    return Counter(row.get(key) or "Unknown" for row in rows)


def count_by_month(rows):
    counts = defaultdict(int)
    for row in rows:
        signup_date = row.get("signup_date")
        if signup_date:
            counts[signup_date.strftime("%Y-%m")] += 1
    return dict(sorted(counts.items()))


def draw_bar_chart(title, counts, color):
    fig, ax = plt.subplots(figsize=(7, 4))
    labels = list(counts.keys())
    values = list(counts.values())
    ax.bar(labels, values, color=color)
    ax.set_title(title)
    ax.set_ylabel("Customers")
    ax.tick_params(axis="x", rotation=35)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    return fig


def draw_pipeline_chart(cleaned_count, rejected_count):
    fig, ax = plt.subplots(figsize=(5, 4))
    ax.bar(["Cleaned", "Rejected"], [cleaned_count, rejected_count], color=["#2f7d59", "#b4493c"])
    ax.set_title("Transform Results")
    ax.set_ylabel("Rows")
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    return fig


def draw_active_chart(rows):
    counts = Counter("Active" if row.get("is_active") else "Inactive" for row in rows)
    fig, ax = plt.subplots(figsize=(5, 4))
    ax.pie(
        [counts["Active"], counts["Inactive"]],
        labels=["Active", "Inactive"],
        autopct="%1.0f%%",
        colors=["#376f9f", "#d18f35"],
        startangle=90,
    )
    ax.set_title("Customer Status")
    fig.tight_layout()
    return fig


st.title("ETL Pipeline Dashboard")

raw_rows, cleaned_rows, rejected_rows = load_pipeline_preview(DEFAULT_CSV)

metric_cols = st.columns(4)
metric_cols[0].metric("Extracted rows", len(raw_rows))
metric_cols[1].metric("Cleaned rows", len(cleaned_rows))
metric_cols[2].metric("Rejected rows", len(rejected_rows))
metric_cols[3].metric("Success rate", f"{(len(cleaned_rows) / len(raw_rows)):.0%}" if raw_rows else "0%")

chart_cols = st.columns([1, 1])
with chart_cols[0]:
    st.pyplot(draw_pipeline_chart(len(cleaned_rows), len(rejected_rows)))
with chart_cols[1]:
    st.pyplot(draw_active_chart(cleaned_rows))

st.subheader("Customer Breakdown")
breakdown_cols = st.columns([1, 1])
with breakdown_cols[0]:
    st.pyplot(draw_bar_chart("Customers by Country", count_by(cleaned_rows, "country"), "#477998"))
with breakdown_cols[1]:
    monthly_counts = count_by_month(cleaned_rows)
    st.pyplot(draw_bar_chart("Signups by Month", monthly_counts, "#8f5b3f"))

tab_raw, tab_cleaned, tab_rejected, tab_database = st.tabs(
    ["Extract", "Transform", "Rejected", "Database"]
)

with tab_raw:
    st.dataframe(raw_rows, use_container_width=True, hide_index=True)

with tab_cleaned:
    st.dataframe(cleaned_rows, use_container_width=True, hide_index=True)

with tab_rejected:
    if rejected_rows:
        st.dataframe(rejected_rows, use_container_width=True, hide_index=True)
    else:
        st.info("No rejected rows in the current CSV.")

with tab_database:
    customer_limit = st.slider("Rows to read from Postgres", min_value=10, max_value=500, value=100, step=10)
    if st.button("Run ETL load"):
        try:
            load_cleaned_rows_to_database(cleaned_rows)
            st.success("Loaded transformed rows into Postgres.")
        except ModuleNotFoundError as exc:
            st.error("Missing Python package needed for Postgres.")
            st.code(f"{exc}\n\nInstall dependencies with: pip install -r requirements.txt")
        except Exception as exc:
            st.error("Could not load rows into Postgres.")
            st.code(str(exc))

    try:
        database_customers = load_database_customers(customer_limit)
    except ModuleNotFoundError as exc:
        st.warning("Install the Postgres dependency before using the Database tab.")
        st.code(f"{exc}\n\nRun: pip install -r requirements.txt")
    except Exception as exc:
        st.warning("Postgres is not available yet. Run the ETL pipeline after starting the database.")
        st.code(str(exc))
    else:
        st.metric("Loaded customers", len(database_customers))
        st.dataframe(database_customers, use_container_width=True, hide_index=True)
