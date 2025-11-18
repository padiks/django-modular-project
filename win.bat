@echo off
REM ----------------------------------
REM Batch file to run Django app
REM ----------------------------------

REM Navigate to the project folder
cd /d C:\laragon\www\dbpilot

REM Optional: pause before running (for debugging)
REM pause

REM Run the Flask app with Python
python manage.py runserver 8000

REM Keep the console open after the app stops
REM pause
