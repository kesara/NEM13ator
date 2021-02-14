# NEM13ator
PoC AEMO (Australian Energy Market Operator) NEM13 file processor

## Setup Python Environment

This application has been tested to Python version 3.7.

Create a Python 3.7 virtual environment and activate.

```
python3.7 -m venv venv
. venv/bin/activate
```

Install required dependencies.

```
pip install -r requirements.txt
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
usage: nem13ator.py [-h] [nem13_file]

AEMO nem13 file processor

positional arguments:
  nem13_file  nem13 file path

optional arguments:
  -h, --help  show this help message and exit
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
