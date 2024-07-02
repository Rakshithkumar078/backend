# CRUD with python flask
## Getting Started

The following prerequisites are required to build and run the solution:

- [python ](https://www.python.org/downloads/) (latest version)

To install all packages required for the projects.
```bash
pip install -r requirements.txt
```

Any new packeges used in the projet, then we need to add that packeges in the requirements.txt file.
```bash
pip freeze > requirements.txt
```

## Migration
to update migration.
```bash
flask db upgrade
```

If you don't have migration versions or not created any migrations then find the bellow commands.

to initialize the migrations.
```bash
flask db init
```

To create the migrations.
```bash
flask db migrate -m "Initial migration(migration name)"
```
## Envirnoment Setup
First, we need to set up the virtual environment for project.
```bash
py -3 -m venv .venv
```
Activate the corresponding environment.
```bash
.venv\Scripts\activate
```
## Run
To run the application
```bash
flask run
```
