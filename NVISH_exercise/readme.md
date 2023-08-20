# Exercise README

## Description

In this Project I have created one app folder which contains exercise related files, and also I have created one folder for testcases
In Exercise folder I created separate python files for exercises. in exercise-3 I have used redis for caching data and use it in API response.


## Table of Contents

- exercise-1
- exercise-2
- exercise-3
- config.py
- models.py
- schema.py
- requirements.txt
- tests
- readme.md
- run.py


## Getting Started
### Prerequisites

#### create virtualenv
-  python3 -m venv myenv
-  source myenv/bin/activate

#### Install requirements

- pip3 install -r requirements.txt

#### Set the FLASK_APP environment variable

- (Unix/Mac) export FLASK_APP=run.py

#### create env file in root directory
- SECRET_KEY = "flasktestapp"
- SQLALCHEMY_DATABASE_URI = "sqlite:///mydatabase1.db"
- FLASK_APP = run
- FLASK_DEBUG = 1


 # Migration  (To create all the models)
 - flask db init
 -  flask db migrate
 - flask db upgrade

 # Run the application

```
## To run the application
```bash

$ python run.py
$ flask run


## To run the test cases
```bash
for run all testcases run 
$ pytest tests

while running testcaes if you get impoertError of app
$  PYTHONPATH=path-to-project-directory  pytest

## Set these environment variables in .env file

SECRET_KEY = "flasktestapp"
SQLALCHEMY_DATABASE_URI = "sqlite:///mydatabase1.db"
FLASK_DEBUG = 1