# markup-cartography
This is serivce for markup territory from coordinates obtained from rosreestr2


### Main functionality:
* **Provides a global map of the area**
* **It is possible to mark the territory along the perimeter of the site by cadastral number (pulled from Rosreestr2coord)**
* **Registration and authorization of users**

### Requirements
* Language: **Python 3.11**
* Framework: **Django**
* Database: **SQLite (you can connect the PostgreSQL/MySQL database)**

## Installation
Install requirements:

    pip install -r requiremets.txt


Fill in the following fields in file settings.py if you connect to PostgreSQL or MySQL database:

        DB_USER = 'user_name'
        DB_PASSWORD = 'your_password'
        DB_HOST = 'your_host'
        DB_NAME = 'your_db_name'


Secret-key for hashing user password:

    SECRET_KEY = 'secret'

## Application launch
After installing all the necessary dependencies and parameters, first run the database migrate script:

    python3 manage.py migrate



###### Or use the terminal, the command to run the application:

    python3 manage.py runserver
