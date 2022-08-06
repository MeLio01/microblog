from datetime import datetime
from flask_login import UserMixin

from project.extensions import db
from project.lib.model_utils import ResourceMixin, generate_uuid

class Post(ResourceMixin, UserMixin, db.Model):
    __tablename__ = "post"

    id = db.Column(db.String(120), unique=True, primary_key=True, index=True, nullable=False, default=generate_uuid)
    body = db.Column(db.String(120))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow())
    user_id = db.Column(db.String(120), db.ForeignKey("user.id"))
    likes = db.relationship('like', lazy='dynamic')
    comments = db.relationship('Comment', lazy='dynamic')