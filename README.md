# lunch_time
This application allows a user to find random colleague to get coffee and lunch

### Assumtions/Approach
1. Lunch friends have no relations with coffee friends in the database.
2. If the system has only 1 user, the app will ask the user to wait when the user tries to find someone to get coffee or lunch.
3. If the system has only 2 users, the user will have a lunch group of 2 people in order to prevent user to eat alone. All the other times, the lunch group will be between 3-5 people.
4. When the user has met with everyone for coffee, the application will ask user to get lunch instead.
5. User can get coffee with only one person.
6. User will be able to find a group for lunch even after having met everyone for lunch before.

### Installation/Startup instructions
This project is run on Django version 1.11.15 and Python2.7. Below are instructions on how to run the project:
1. Create a folder to install Django environment
2. Navigate to the folder
3. Follow the instructions to install Django:
    ```
    virtualenv djangoEnv
    source djangoEnv/bin/activate
    pip install django
    ```
4. Create another folder in a different location and clone this git repository in that folder
5. Navigate to lunch_time and locate manage.py in the directory
The correct location will look something like this:
```
README.md	apps		db.sqlite3	manage.py	registration
```
7. Run this command in the terminal: ```python2.7 manage.py runserver```
8. Type in ```http://localhost:8000``` in the browser


### Python 2.7 Installation
If Python 2.7 is not installed in the machine, it can be downloaded from here: https://www.python.org/downloads/
