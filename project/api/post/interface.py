from dataclasses import dataclass
from typing import Dict, Any

from .model import Post as PostDB

@dataclass
class Post:
    id: str
    body: str
    timestamp: str
    user_id: str

    @classmethod
    def instance_creator(cls, post_db: PostDB):
        return cls(
            id = post_db.id,
            body = post_db.body,
            timestamp = post_db.timestamp,
            user_id = post_db.user_id
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