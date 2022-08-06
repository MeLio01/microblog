from project.extensions import db
from project.lib.model_utils import ResourceMixin, generate_uuid


class Comment(ResourceMixin, db.Model):
    __tablename__ = "Comment"

    id = db.Column(db.String(120), primary_key=True, unique=True, index=True, nullable=False, default=generate_uuid)
    userid = db.Column(db.String(120), db.ForeignKey('user.id'), primary_key=True)
    postid = db.Column(db.String(120), db.ForeignKey('post.id'), primary_key=True)
    body = db.Column(db.String(240), nullable=False)