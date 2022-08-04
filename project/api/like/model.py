from project.extensions import db
from project.lib.model_utils import ResourceMixin

class like(ResourceMixin, db.Model):
    __tablename__ = "like"

    userid = db.Column(db.String(120), db.ForeignKey('user.id'), primary_key=True)
    postid = db.Column(db.String(120), db.ForeignKey('post.id'), primary_key=True)
