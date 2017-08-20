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

### 1. Models
Two models created:
- Meal - represents a single meal
- Card - represents menu card
### 2. Views
Five views created:
- CardListView - renders template for list of menu cards
- CardDetailView - renders template for single menu card
- CardListAPIView - renders API for list of menu cards
- CardRetrieveAPIView - renders API for single menu card
- FinalView - renders template for list of menu cards. This view bases on CardListAPIView. The data was consumed from API, paginated and displayed in a table

### 3. Sorting
Sorting by id, name or number of meals was achieved thanks to JS tablesorter implemented.

_some more documentation can be found here:_
http://127.0.0.1:8000/admin/doc/

## Tests
Tests can be run by:

- ```python manage.py test menu```

or if coverage report shall be generated, this commands should be used:
- ```coverage run --source='.' manage.py test menu```
- ```coverage report --include="./menu/*"```


@created by brzydal
