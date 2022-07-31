from datetime import datetime

from project.extensions import db
from project.lib.model_utils import ResourceMixin, generate_uuid

class follow(ResourceMixin, db.Model):
    __tablename__ = "follow"

    id = db.Column(db.String(120), unique=True, primary_key=True, index=True, nullable=False, default=generate_uuid)
    follower_id = db.Column(db.String(120), db.ForeignKey('user.id'))
    followed_id = db.Column(db.String(120), db.ForeignKey('user.id'))