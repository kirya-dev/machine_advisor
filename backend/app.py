import os

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import yaml


def load_config():
    path = os.environ.get('BACKEND_CONFIG', 'config.yml')
    with open(path) as fp:
        return yaml.load(fp)


app = Flask(__name__)
app.config.update(load_config())

cors = CORS(app, max_age=86400)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

ma = Marshmallow(app)  # For serialize objects
