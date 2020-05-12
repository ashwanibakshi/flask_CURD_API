from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost:3306/flasktest'

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app,db)

import route

if __name__ == '__main__':
    app.run()