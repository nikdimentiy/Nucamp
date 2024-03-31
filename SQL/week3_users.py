from flask import Blueprint, jsonify, abort, request
from sqlalchemy.exc import SQLAlchemyError
from ..models import User, Tweet, likes_table, db
import sqlalchemy
import hashlib
import secrets

# Blueprint initialization
bp = Blueprint('users', __name__, url_prefix='/users')

# Error handler for 400 Bad Request
@bp.app_errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "Bad Request"
    }), 400

# Helper function to hash and salt password
def scramble(password: str):
    """Hash and salt the given password"""
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()

# Route to fetch all users
@bp.route('', methods=['GET'])
def index():
    try:
        users = User.query.all()
        result = [user.serialize() for user in users]
        return jsonify(result)
    except SQLAlchemyError:
        return abort(400)

# Route to fetch a specific user by ID
@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    user = User.query.get_or_404(id)
    try:
        return jsonify(user.serialize())
    except SQLAlchemyError:
        return abort(400)

# Route to fetch all tweets liked by a user
@bp.route('/<int:id>/liked_tweets', methods=['GET'])
def liked_tweets(id: int):
    user = User.query.get_or_404(id)
    try:
        liked_tweets = [tweet.serialize() for tweet in user.liked_tweets]
        return jsonify(liked_tweets)
    except SQLAlchemyError:
        return abort(400)

# Route to create a new user
@bp.route('', methods=['POST'])
def create():
    if 'username' not in request.json or 'password' not in request.json:
        return abort(400)
    if len(request.json['username']) < 3 or len(request.json['password']) < 8:
        return abort(400)
    try:
        user = User(
            username=request.json['username'],
            password=scramble(request.json['password'])
        )
        db.session.add(user)
        db.session.commit()
        return jsonify(user.serialize()), 201  # HTTP 201 Created
    except SQLAlchemyError:
        db.session.rollback()
        return abort(400)

# Route to like a tweet
@bp.route('/<int:id>/likes', methods=['POST'])
def like(id: int):
    if 'tweet_id' not in request.json:
        return abort(400)
    user = User.query.get_or_404(id)
    tweet = Tweet.query.get_or_404(request.json['tweet_id'])
    try:
        stmt = sqlalchemy.insert(likes_table).values(
            tweet_id=tweet.id, user_id=user.id)
        db.session.execute(stmt)
        db.session.commit()
        return jsonify(True)
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify(False)

# Route to unlike a tweet
@bp.route('/<int:user_id>/likes/<int:tweet_id>', methods=['DELETE'])
def unlike(user_id: int, tweet_id: int):
    user = User.query.get_or_404(user_id)
    tweet = Tweet.query.get_or_404(tweet_id)
    try:
        stmt = sqlalchemy.delete(likes_table).where(
            sqlalchemy.and_(
                likes_table.c.user_id == user_id,
                likes_table.c.tweet_id == tweet_id
            )
        )
        db.session.execute(stmt)
        db.session.commit()
        return jsonify(True)
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify(False)

# Route to delete a user
@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    user = User.query.get_or_404(id)
    try:
        db.session.delete(user)
        db.session.commit()
        return jsonify(True)
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify(False)

# Route to update user information
@bp.route('/<int:id>', methods=['PATCH'])
def update(id: int):
    user = User.query.get_or_404(id)
    if 'username' in request.json:
        user.username = request.json['username']
    if 'password' in request.json:
        user.password = scramble(request.json['password'])
    try:
        db.session.commit()
        return jsonify(True)
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify(False)
