import connexion
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

connextion_app = connexion.App(__name__, specification_dir='config/api')
connextion_app.add_api('swagger.yml')

URL_SQL = os.path.join(basedir, 'db.sqlite3')

app = connextion_app.app
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{URL_SQL}'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

from pybookstore import routes
