import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Define the association table for the many-to-many relationship between users and tweets
likes_table = db.Table(
    'likes',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('tweet_id', db.Integer, db.ForeignKey('tweets.id'), primary_key=True),
    db.Column('created_at', db.DateTime, default=datetime.datetime.utcnow, nullable=False)
)


class User(db.Model):
    __tablename__ = 'users'

    # Define columns for the User table
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    # Define relationship with tweets posted by the user
    tweets = db.relationship('Tweet', backref='user', cascade="all,delete")

    # Define relationship with tweets the user has liked
    liked_tweets = db.relationship(
        'Tweet', secondary=likes_table,
        lazy='subquery',
        backref=db.backref('liked_by_users', lazy=True)
    )

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def serialize(self):
        """Serialize User object to JSON"""
        return {
            'id': self.id,
            'username': self.username
        }


class Tweet(db.Model):
    __tablename__ = 'tweets'

    # Define columns for the Tweet table
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(280), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)

    # Define relationship with the user who posted the tweet
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # Define relationship with users who have liked the tweet
    liked_by_users = db.relationship(
        'User', secondary=likes_table,
        lazy='subquery',
        backref=db.backref('liked_tweets', lazy=True)
    )

    def __init__(self, content: str, user_id: int):
        self.content = content
        self.user_id = user_id

    def serialize(self):
        """Serialize Tweet object to JSON"""
        return {
            'id': self.id,
            'content': self.content,
            'created_at': self.created_at.isoformat(),
            'user_id': self.user_id
        }
