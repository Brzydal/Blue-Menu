# Blue-Menu
Project created as a part of an interview process in Blue Services.
The idea of a project was to develop a simple app which can be used for creation and management for restaurant menu cards.

## Set Up

### 1. Install basic requirements:
#### Requirements
- Python 2.7.12
- PostgreSQL 9.5.7
- VirtualEnv 15.0.1
- Git 2.7.4

### 2. Download repository from GitHub:
https://github.com/Brzydal/Blue-Menu
- ```git clone https://github.com/Brzydal/Blue-Menu.git```

### 3. Virtualenv:
- install virtualenv: ```pip install virtualenv```
- create sandbox: ```virtualenv <directory>```
- and activate it: ```source <directory>/bin/activate```

### 4. Install other requirements:
All other requirements as per requirements.txt:
https://github.com/Brzydal/Blue-Menu/blob/master/requirements.txt
- ```pip install -r requirements.txt```

### 5. Database configuration:
- create superuser damian: ```sudo -u postgres createuser --superuser damian```
- with password damian: ```sudo -u postgres psql``` and ```postgres=# \password damian```
- create database menu_db: ```sudo -u postgres createdb -0 damian menu_db```
- fill up database with data: Go to Blue Menu/db_data and run ```psql menu_db < menu_db_dump``` or run all SQL queries in Blue Menu/db_data.
- check db configuration in settings.py
    ```Python
    DATABASES = {
        'default': {
            'HOST': '127.0.0.1',
            'NAME': 'menu_db',
            'ENGINE': 'django.db.backends.postgresql',
            'USER': 'damian',
            'PASSWORD': 'damian',
        }
    }
    ```
### 6. Start the app and Bon Apetit!
- ```python manage.py runserver```


## Features

## Tests
- ```python manage.py menu test```

create superuser

@created by brzydal
