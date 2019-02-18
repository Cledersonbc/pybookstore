import connexion
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

connexion_app = connexion.App(__name__, specification_dir='config/api')

app = connexion_app.app
app.config.from_object('pybookstore.settings.local')
db = SQLAlchemy(app)
ma = Marshmallow(app)

connexion_app.add_api('swagger.yml')

from pybookstore import routes
