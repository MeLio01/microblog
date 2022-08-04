from dataclasses import dataclass


from dataclasses import dataclass
from typing import Dict, Any

from .model import like as likeDB

from project.extensions import db

@dataclass
class like:
    userid : str
    postid : str

    @classmethod
    def instance_creator(cls, likes_db: likeDB):
        return cls(
            userid = likes_db.userid,
            postid = likes_db.postid
        )
    
    @classmethod
    def add_like(cls, likeinfo: Dict[str, Any]):
        like_db = likeDB(
            userid=likeinfo["userid"],
            postid=likeinfo["postid"]
        )
        like_db.create()
        if like_db:
            return cls.instance_creator(like_db)
        return None
    
    @classmethod
    def delete_like(cls, likeinfo: Dict[str, Any]):
        like_db: likeDB = likeDB.query.filter_by(userid=likeinfo["userid"], postid=likeinfo["postid"]).first()
        if like_db:
            db.session.delete(like_db)
            db.session.commit()
            return True
        return False