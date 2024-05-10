from flask import Flask
import os


def create_app(debug=None) -> Flask:
    # Initialize app
    app = Flask(
        __name__,
        template_folder='../templates',
        static_folder='../static',
        static_url_path='/assets/'
        )
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


    # # Initialize extensions
    from app.modules import db
    db.init_app(app)
    # csrf.init_app(app)
    # bcrypt.init_app(app)
    # login_manager.init_app(app)

    # Create database tables
    from app import models
    with app.app_context():
        db.create_all()

    # Register blueprints
    from app.routes import routes_bp
    app.register_blueprint(routes_bp)

    return app
