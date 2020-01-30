"""SQLAlchemy models for TwitOff"""
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class User(DB.Model):
    """Twitter users that we query and store historical tweets"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String(20), nullable=False)
    followers = DB.Column(DB.BigInteger, nullable=False)
    # Tweet IDS are ordinal ints, so we can fetch most recent tweets
    newest_tweet_id = DB.Column(DB.BigInteger, nullable=False)

    # def __repr__(self):
    #     return 'User {}, Followers {} deg'.format(self.name, self.followers)

class Tweets(DB.Model):
    """Stores tweets"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(300), nullable=False)
    embedding = DB.Column(DB.PickleType, nullable=False)
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey('user.id'), nullable=False)
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))
