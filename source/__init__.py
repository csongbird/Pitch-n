from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()


def create_app():
    from .app import app as flask_app
    flask_app.config['SECRET_KEY'] = 'secret-key-goes-here'
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    db.init_app(flask_app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(flask_app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from .app import auth as auth_blueprint
    flask_app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    flask_app.register_blueprint(main_blueprint)

    return flask_app
