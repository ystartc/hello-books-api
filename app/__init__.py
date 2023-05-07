from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app(test_config=None):
    app = Flask(__name__)
    
    if test_config:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('TEST_DB_URI')
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DEV_DB_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    from app.models.book import Book
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    from .route import books_bp
    app.register_blueprint(books_bp)
    
    from .route_author import authot_bp
    app.register_blueprint(authot_bp)
    
    return app
