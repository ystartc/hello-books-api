from flask import Blueprint, abort, jsonify, make_response, request
from app.models.book import Book
from app import db


books_bp = Blueprint('books', __name__, url_prefix='/books')

# helper function:
def validate_id(model, id):
    if not id.isnumeric():
        abort(make_response({'Error': f'{model.__name__} id# {id} is invalid'}, 400))
    
    entity = model.query.get(id)  
    if not entity:
        abort(make_response({'Error': f'{model.__name__} id#{id} is not found'}, 404))
        
    return entity

# routes: 
@books_bp.route('', methods=['POST'])
def create_book():
    request_body = request.get_json()
    if 'title' not in request_body or 'description' not in request_body:
        abort(make_response({'Error': 'Invalid Request'}, 400))
    
    new_book = Book.from_dict(request_body)
    
    db.session.add(new_book)
    db.session.commit()
    
    return {'msg': f'Book {new_book.title} created'}, 201
 
@books_bp.route('', methods=['GET'])
def read_books():
    title_query = request.args.get('title')
    if title_query:
        books = Book.query.filter(Book.title.ilike(title_query+'%'.strip()))
    else:
        books = Book.query.all()

    book_response = [book.to_dict() for book in books]
    return jsonify(book_response), 200

@books_bp.route('/<book_id>', methods=['GET'])
def get_one_book(book_id):
    book = validate_id(Book, book_id)
    
    return book.to_dict(), 200

@books_bp.route('/<book_id>', methods=['PUT'])   
def replace_book(book_id):
    book = validate_id(Book, book_id)
    
    request_body = request.get_json()
    
    book.title = request_body['title']
    book.description = request_body['description']
    
    db.session.commit()
    
    return {'msg': f'Book {book_id} successfully updated'}, 200

@books_bp.route('/<book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = validate_id(Book, book_id)
    
    db.session.delete(book)
    db.session.commit()
    
    return {'msg': f'Book {book_id} successfully deleted'}, 200
















# class Book:
#     def __init__(self, id, title, genre, description, year):
#         self.id = id
#         self.title = title
#         self.genre = genre
#         self.description = description
#         self.year = year
        
# book_descripion = "A series of seven fantasy novels written by British author J. K. Rowling. The novels chronicle the lives of a young wizard, Harry Potter, and his friends Hermione Granger and Ron Weasley, all of whom are students at Hogwarts School of Witchcraft and Wizardry."

# books = [
#     Book(1, "Harry Potter and the Sorcerer’s Stone", "Fantasy", book_descripion, 1997),
#     Book(2, "Harry Potter and the Chamber of Secrets", "Fantasy", book_descripion, 1998),
#     Book(3, "Harry Potter and the Prisoner of Azkaban", "Fantasy", book_descripion, 1999),
#     Book(4, "Harry Potter and the Goblet of Fire ", "Fantasy", book_descripion, 2000 ),
#     Book(5, "Harry Potter and the Order of the Phoenix", "Fantasy", book_descripion, 2003),
#     Book(6, "Harry Potter and the Half-Blood Prince ", "Fantasy", book_descripion, 2005),
#     Book(7, "Harry Potter and the Deathly Hallows", "Fantasy", book_descripion, 2007)
#          ]

# def validate_book_id(book_id):
#     try:
#         int(book_id)
#     except:
#         abort(make_response({'Error': f'Book id# {book_id} is invalid'}, 400))
        
#     book = [vars(book) for book in books if book.id == int(book_id)]
#     if not book:
#         abort(make_response({'Error': f'Book id# {book_id} is not found'}, 404))
#     return book[0]
    
# books_bp = Blueprint('books', __name__, url_prefix='/books')

# @books_bp.route('', methods=['GET'])
# def get_books():
#     return jsonify([vars(book) for book in books]), 200

# @books_bp.route('/<book_id>', methods=['GET'])
# def get_one_book(book_id):
#     return jsonify(validate_book_id(book_id)), 200