<b>Set FLASK_APP</b>

The FLASK_APP environment variable is used to specify how to load the application.

Unix Bash (Linux, Mac, etc.):

export FLASK_APP=app.py

Windows CMD: 
set FLASK_APP=app.py

Windows PowerShell: 
$env:FLASK_APP = 'app.py'

<b>Add MigrationFolder</b>

flask db init

flask db migrate

flask db upgrade

refresh the table in database you see the table there.

<b> Run App</b>

 flask run
