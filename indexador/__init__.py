from flask import Flask 

from .commands import create_tables
from .commands import insert_data

from .routes.main import main

def create_app(config_file='settings.py'):
    app = Flask(__name__)


    app.register_blueprint(main)


    app.cli.add_command(create_tables)
    app.cli.add_command(insert_data)

    return app