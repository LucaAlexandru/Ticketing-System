@ECHO OFF
ECHO This bat file sets the current working directory and runs the Django manage.py file which boots up the server.
python "%cd%/manage.py" runserver
PAUSE