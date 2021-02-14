# NEM13ator
PoC AEMO (Australian Energy Market Operator) NEM13 file processor

## Setup Python Environment

This application has been tested to Python version 3.7.

Create a Python 3.7 virtual environment and activate.

```
python3.7 -m venv venv
. venv/bin/activate
```

### Setup database
By default SQLite database gets created at `data/main.db`.

```
python data/migrations/db_0000_initial.py
```

## Processing NEM13 files

```
python nem13ator.py <nem13_file>
```

Example:

```
python nem13ator.py tests/data/AEMO556810778013NEM13.csv
```

### Usage

```
usage: nem13ator.py [-h] [--database [DATABASE]] [nem13_file]

AEMO nem13 file processor

positional arguments:
  nem13_file            nem13 file path (required)

optional arguments:
  -h, --help            show this help message and exit
  --database [DATABASE]
                        SQLite database file location (optional)
```

## Running tests

Install required dependencies for testing.

```
pip install -r requirements.dev.txt
```

Run unit tests.

```
python -m unittest discover tests -p "*.py"
```

## Running security tests

Install required dependencies for testing.

```
pip install -r requirements.sec.txt
```

Run security tests.

```
bandit -r nem13ator.py nem13ator
```

## TODO / Improvements
* Add tests for `datastore.py`.
* Improve existing tests and use [hypothesis](https://hypothesis.readthedocs.io/).
* Use [psycopg2](https://www.psycopg.org/) or [SQLAlchemy](https://www.sqlalchemy.org/) with PostreSQL.
* Use a proper database migration process like [Alembic](https://alembic.sqlalchemy.org/en/latest/).
* Improve database schema to store additional information.
* Add the moment, readings are recorded regardless whether they are already
exists or they are more recent readings for a given register exists in the
system, this has to be improved.
