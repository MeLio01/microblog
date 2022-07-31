from dataclasses import dataclass
from typing import Dict, Any

from .model import follow as followDB

from project.api.post import PostDB
from project.api.user import UserDB

from project.extensions import db

@dataclass
class follow:
    id: str
    follower_id: str
    followed_id: str

    @classmethod
    def instance_creator(cls, follow_db: followDB):
        return cls(
            id = follow_db.id,
            follower_id = follow_db.follower_id,
            followed_id = follow_db.followed_id
        )
    
    @classmethod
    def follow(cls, followinfo: Dict[str, Any]):
        follow_db = followDB(
            follower_id=followinfo["follower_id"],
            followed_id=followinfo["followed_id"]
        )
        follow_db.create()
        if follow_db:
            follow_user_db = UserDB.get_first({"id": followinfo["followed_id"]})
            return cls.instance_creator(follow_db)
        return None
    
    @classmethod
    def unfollow(cls, followinfo: Dict[str, Any]):
        follow_db: followDB = followDB.get_first({"id": followinfo["id"]})
        if follow_db:
            db.session.delete(follow_db)
            db.session.commit()
            return True
        return False
    
    @classmethod
    def get_follow_by_id(cls, followinfo: Dict[str, Any]):
        follow_db: followDB = followDB.get_first({"id": followinfo["id"]})
        if follow_db:
            return cls.instance_creator(follow_db)
        return None