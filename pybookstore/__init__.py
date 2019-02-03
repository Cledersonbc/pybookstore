import connexion
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

connextion_app = connexion.App(__name__, specification_dir='config/api')
connextion_app.add_api('swagger.yml')

sql_string = 'sqlite:///' + os.path.join(basedir, 'book.db')
app = connextion_app.app
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = sql_string
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

from pybookstore import routes
