from flask import Blueprint, abort, jsonify, make_response, request
from app.models.book import Book
from app import db


authot_bp = Blueprint('authors', __name__, url_prefix='/authors')