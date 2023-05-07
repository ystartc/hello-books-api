from flask.signals import request_finished
import pytest
from app import create_app, db
from app.models.book import Book

@pytest.fixture
def app():
    app = create_app({'TESTING': True})
    
    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()
            
    with app.app_context():
        db.create_all()
        yield app
        
    with app.app_context():
        db.drop_all()

@pytest.fixture       
def client(app):
    return app.test_client()

@pytest.fixture
def add_two_books(app):
    warriors_book = Book(title='Warriors', description='best team ever')
    lakers_book = Book(title='Lakers', description='the team to beat')
    
    db.session.add_all([warriors_book, lakers_book])
    db.session.commit()
