# Data Foundations

Welcome to the Data Foundations course repository. This repo contains supplemental notes, project requirements, and presentation guidance you will use during the course.

## How to Use This Repo

Start here when you need to review course concepts, revisit examples from class, or check expectations for the final project.

Recommended flow:

1. Review the weekly notes for the topic you are studying.
2. Use the project requirements to guide your build.
3. Use the presentation guidelines when preparing your demo.
4. Keep your own code, notes, and project work organized in your assigned project repository or workspace.

## Course Focus

By the end of this course, you should be more comfortable with:

- Writing Python programs using clear structure, functions, classes, and modules.
- Working with files, JSON, CSV data, logging, exceptions, and testing.
- Using Git and GitHub as part of a professional development workflow.
- Querying and designing relational databases with PostgreSQL.
- Building a small data ingestion pipeline that reads, validates, cleans, and loads data.
- Explaining your technical work clearly in a short project presentation.

## Final Project

The final project is a Data Ingestion Subsystem. You will build a Python-based pipeline that can read data from one or more sources, validate and clean the data, and load it into a PostgreSQL database.

At a high level, your project should demonstrate:

- Data extraction from CSV, JSON, an API, or another approved source.
- Validation and cleaning logic for messy or inconsistent records.
- Duplicate handling.
- Loading into PostgreSQL tables.
- Logging or reporting for each ingestion run.
- Tests for important behavior.
- A short demo that explains the problem, solution, architecture, implementation, and next steps.

Read the full project expectations here: [project/requirements.md](project/requirements.md)

Presentation guidance: [project/etl-presentation-guidelines.md](project/etl-presentation-guidelines.md)

## Optional Project Structure

You may organize your implementation differently, but a structure like this is a great:

```text
ingestion/
  src/
    readers/
    config.py
    validate.py
    clean.py
    load.py
    main.py
  config/
  data/
  sql/
  tests/
  requirements.txt
  README.md
```

## Student Expectations

- Ask questions early when you are blocked.
- Read the weekly notes before asking for help on a topic covered in class.
- Keep your project code readable, modular, and named clearly.
- Use Git regularly and write meaningful commit messages in your own project work.
- Do not commit secrets, passwords, API keys, `.env` files, virtual environments, or large generated files.
- Be ready to explain not only what your code does, but why your team made those design choices.

## Helpful Local Setup

For Python work, use a virtual environment:

```bash
python -m venv .venv
```

Activate it:

```bash
# Windows PowerShell
.\.venv\Scripts\Activate.ps1

# macOS/Linux
source .venv/bin/activate
```

Install dependencies from a project `requirements.txt` when available:

```bash
pip install -r requirements.txt
```
