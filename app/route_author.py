from flask import Blueprint, abort, jsonify, make_response, request
from app.models.author import Author
from app import db


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