from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()


def create_app():


    app = Flask(__name__)
    app.debug = True
    app.secret_key = 'somethingsecret'
    #c config the image upload
    UPLOAD_FOLDER = '/static/image'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    # config the db
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///travel_data.sqlite'
    # initialise
    db.init_app(app)

    bootstrap = Bootstrap(app)

    from . import errors
    app.register_blueprint(errors.bp)

    from . import views
    app.register_blueprint(views.mainbp)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import destinations
    app.register_blueprint(destinations.bp)

    # initialize the login manager
    login_manager = LoginManager()
    # set the name of the login function that lets user login
    # in our case it is auth.login (blueprintname.viewfunction name)
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # create a user loader function takes userid and returns User
    from .models import User  # importing here to avoid circular references

    @login_manager.user_loader  
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app
