from dataclasses import dataclass


from dataclasses import dataclass
from typing import Dict, Any

from .model import Comment as CommentDB

from project.extensions import db

@dataclass
class Comment:
    id : str
    userid : str
    postid : str
    body : str

    @classmethod
    def instance_creator(cls, comment_db: CommentDB):
        return cls(
            id = comment_db.id,
            userid = comment_db.userid,
            postid = comment_db.postid,
            body = comment_db.body
        )
    
    @classmethod
    def add_comment(cls, Commentinfo: Dict[str, Any]):
        comment_db = CommentDB(
            userid=Commentinfo["userid"],
            postid=Commentinfo["postid"],
            body=Commentinfo["body"]
        )
        comment_db.create()
        if comment_db:
            return cls.instance_creator(comment_db)
        return None

    @classmethod
    def delete_comment(cls, commentinfo: Dict[str, Any]):
        comment_db: CommentDB = CommentDB.query.filter_by(id=commentinfo["id"]).first()
        if comment_db:
            db.session.delete(comment_db)
            db.session.commit()
            return True
        return False
    
    @classmethod
    def update_comment(cls, commentinfo: Dict[str, Any]):
        comment_db: CommentDB = CommentDB.get_first({"id": commentinfo["id"]})
        if comment_db:
            comment_db = comment_db.update(**commentinfo)
            return cls.instance_creator(comment_db)
        return None

    @classmethod
    def get_comment(cls, commentinfo: Dict[str, Any]):
        comment_db: CommentDB = CommentDB.get_first({"id": commentinfo["id"]})
        if comment_db:
            return cls.instance_creator(comment_db)
        return None