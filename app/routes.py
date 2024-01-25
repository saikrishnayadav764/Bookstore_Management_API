from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from .models import book_schema
from .auth import login 

bp = Blueprint('main', __name__, url_prefix='/api')

# Adding a new book
@bp.route('/books', methods=['POST'])
@jwt_required()
def add_book():
    from . import mongo
    data = request.get_json()

    mongo.db.books.insert_one(data)
    return jsonify({"message": "Book added successfully"}), 201

# Retrieving all books
@bp.route('/books', methods=['GET'])
@jwt_required()
def get_books():
    from . import mongo
    books = list(mongo.db.books.find({}, {'_id': 0}))
    return jsonify(books), 200

# Retrieving a specific book by ISBN
@bp.route('/books/<ISBN>', methods=['GET'])
@jwt_required()
def get_book(ISBN):
    from . import mongo
    book = mongo.db.books.find_one({"ISBN": ISBN}, {'_id': 0})
    if book:
        return jsonify(book), 200
    return jsonify({"message": "Book not found"}), 404

# Updating book details
@bp.route('/books/<ISBN>', methods=['PUT'])
@jwt_required()
def update_book(ISBN):
    from . import mongo
    data = request.get_json()
    result = mongo.db.books.update_one({"ISBN": ISBN}, {"$set": data})
    if result.modified_count == 1:
        return jsonify({"message": "Book updated successfully"}), 200
    return jsonify({"message": "Book not found"}), 404

# Deleting a book
@bp.route('/books/<ISBN>', methods=['DELETE'])
@jwt_required()
def delete_book(ISBN):
    from . import mongo
    result = mongo.db.books.delete_one({"ISBN": ISBN})
    if result.deleted_count == 1:
        return jsonify({"message": "Book deleted successfully"}), 200
    return jsonify({"message": "Book not found"}), 404


