from datetime import datetime
from flask_login import UserMixin

from project.extensions import db
from project.lib.model_utils import ResourceMixin, generate_uuid

class User(ResourceMixin, UserMixin, db.Model):
    __tablename__ = "user"

    id = db.Column(db.String(120), unique=True, primary_key=True, index=True, nullable=False, default=generate_uuid)
    username = db.Column(db.String(120), unique=True, index=True, nullable=False)
    email = db.Column(db.String(120), unique=True, index=True, nullable=False)
    password_hash = db.Column(db.String(128))
    about_me = db.Column(db.String(200))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow())
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    likes = db.relationship('like', lazy='dynamic')
    followed = db.relationship('follow', foreign_keys='follow.follower_id', backref=db.backref('follower', lazy='joined'), lazy='dynamic')
    followers = db.relationship('follow', foreign_keys='follow.followed_id', backref=db.backref('followed', lazy='joined'), lazy='dynamic')
    comments = db.relationship('Comment', lazy='dynamic')