from dataclasses import dataclass
from typing import Dict, Any

from .model import Post as PostDB

from project.api.user import UserDB

from project.extensions import db

@dataclass
class Post:
    id: str
    body: str
    timestamp: str
    user_id: str
    likes: tuple
    comments: tuple

    @classmethod
    def instance_creator(cls, post_db: PostDB):
        return cls(
            id = post_db.id,
            body = post_db.body,
            timestamp = post_db.timestamp,
            user_id = post_db.user_id,
            likes = post_db.likes,
            comments = post_db.comments
        )

    @classmethod
    def add_post(cls, postinfo: Dict[str, Any]):
        post_db = PostDB(
            user_id = postinfo["user_id"],
            body = postinfo["body"]
        )
        post_db.create()
        if post_db:
            return cls.instance_creator(post_db)
        return None
    
    @classmethod
    def update_post(cls, postinfo: Dict[str, Any]):
        post_db: PostDB = PostDB.get_first({"id": postinfo["id"]})
        if post_db:
            post_db = post_db.update(**postinfo)
            return cls.instance_creator(post_db)
        return None
    
    @classmethod
    def post_by_id(cls, postinfo: Dict[str, Any]):
        post_db: PostDB = PostDB.get_first({"id": postinfo["id"]})
        if post_db:
            return cls.instance_creator(post_db)
        return None

    @classmethod
    def delete_post(cls, postinfo: Dict[str, Any]):
        post_db: PostDB = PostDB.get_first({"id": postinfo["id"]})
        if post_db:
            db.session.delete(post_db)
            db.session.commit()
            return True
        return False
    
    @classmethod
    def get_likes(cls, postinfo: Dict[str, Any]):
        post_db: PostDB = PostDB.get_first({"id": postinfo["id"]})
        if post_db:
            return tuple([like.userid for like in post_db.likes])
        return None
    
    @classmethod
    def get_comments(cls, postinfo: Dict[str, Any]):
        post_db: PostDB = PostDB.get_first({"id": postinfo["id"]})
        if post_db:
            return tuple([comment.id for comment in post_db.comments])
        return None