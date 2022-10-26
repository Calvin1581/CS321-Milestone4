from venv import create
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from pathlib import Path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"
# the location of the csv upload folder
UPLOAD_FOLDER = "./csvs"


def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # configure an upload folder for csv uploads
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    db.init_app(app)

    from .views import views
    from .auth import auth
    # from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    # app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note
    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app: Flask):
    if not path.exists('website/' + DB_NAME):
        print('Created Database!')

        # use app context in order to initialize properly
        with app.app_context():
            db.create_all()
