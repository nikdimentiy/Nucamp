from flask import Blueprint, jsonify, abort, request
from sqlalchemy.exc import SQLAlchemyError
from ..models import Tweet, User, db

bp = Blueprint('tweets', __name__, url_prefix='/tweets')


@bp.app_errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "Bad Request"
    }), 400


@bp.route('', methods=['GET'])
def index():
    try:
        tweets = Tweet.query.all()
        result = [tweet.serialize() for tweet in tweets]
        return jsonify(result)
    except SQLAlchemyError:
        return abort(400)


@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    tweet = Tweet.query.get_or_404(id)
    try:
        return jsonify(tweet.serialize())
    except SQLAlchemyError:
        return abort(400)


@bp.route('/<int:id>/liking_users', methods=['GET'])
def liking_users(id: int):
    tweet = Tweet.query.get_or_404(id)
    try:
        liking_users = [user.serialize() for user in tweet.likes]
        return jsonify(liking_users)
    except SQLAlchemyError:
        return abort(400)


@bp.route('', methods=['POST'])
def create():
    if 'user_id' not in request.json or 'content' not in request.json:
        return abort(400)

    user = User.query.get_or_404(request.json['user_id'])
    try:
        tweet = Tweet(
            user_id=request.json['user_id'],
            content=request.json['content']
        )
        db.session.add(tweet)
        db.session.commit()
        return jsonify(tweet.serialize()), 201  # HTTP 201 Created
    except SQLAlchemyError:
        db.session.rollback()
        return abort(400)


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    tweet = Tweet.query.get_or_404(id)
    try:
        db.session.delete(tweet)
        db.session.commit()
        return jsonify(True)
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify(False)
