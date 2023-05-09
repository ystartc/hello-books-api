from flask import Blueprint, abort, jsonify, make_response, request
from app.models.author import Author
from app.models.book import Book
from app import db
from .route import validate_id


author_bp = Blueprint('authors', __name__, url_prefix='/authors')


@author_bp.route('', methods=['POST'])
def create_author():
    request_body = request.get_json()
    
    new_author = Author.from_dict(request_body)
    
    db.session.add(new_author)
    db.session.commit()
    
    return {'msg': f'Author {new_author.name} record created'}, 201

@author_bp.route('', methods=['GET'])
def get_authors():
    authors = Author.query.all()
    
    author_response = [author.to_dict() for author in authors]
    
    return jsonify(author_response), 200

@author_bp.route('/<author_id>/books', methods=['POST'])
def create_book(author_id):
    author = validate_id(Author, author_id)
    request_body = request.get_json()
    
    new_book = Book(
                    title=request_body['title'],
                    description=request_body['description'],
                    author=author)
    
    db.session.add(new_book)
    db.session.commit()
    
    return {'msg': f'Book {new_book.title} by {new_book.author.name} created'}, 201

@author_bp.route('/<author_id>/books', methods=['GET'])
def get_books_by_author(author_id):
    author = validate_id(Author, author_id)
    
    # books = Book.query.filter(Author.id == author_id)
    book_response = [book.to_dict() for book in author.books]
    # book_response = [book.to_dict().update({'author': author.name}) for book in books]
    # book_response = [book.to_dict() for book in books]
    
    return jsonify(book_response), 200