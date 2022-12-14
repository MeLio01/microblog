from dataclasses import dataclass
from typing import Dict, Any
from werkzeug.security import generate_password_hash, check_password_hash

from .model import User as UserDB


@dataclass
class User:
    id: str
    username: str
    email: str
    password_hash: str
    about_me: str
    last_seen: str
    posts: tuple
    likes: tuple
    followed: tuple
    followers: tuple
    comments: tuple

    @classmethod
    def instance_creator(cls, user_db: UserDB):
        return cls(
            id = user_db.id,
            username = user_db.username,
            email = user_db.email,
            password_hash = user_db.password_hash,
            about_me = user_db.about_me,
            last_seen = user_db.last_seen,
            posts = user_db.posts,
            likes = user_db.likes,
            followed = user_db.followed,
            followers = user_db.followers,
            comments = user_db.comments
        )
    
    @classmethod
    def add_user(cls, userinfo: Dict[str, Any]):
        user_db = UserDB(
            username=userinfo["username"],
            email=userinfo["email"],
            password_hash=generate_password_hash(userinfo["password_hash"])
        )
        user_db.create()
        if user_db:
            return cls.instance_creator(user_db)
        return None
    
    @classmethod
    def update_user(cls, userinfo: Dict[str, Any]):
        user_db: UserDB = UserDB.get_first({"id": userinfo["id"]})
        if user_db:
            user_db = user_db.update(**userinfo)
            return cls.instance_creator(user_db)
        return None
    
    @classmethod
    def delete_user(cls, userinfo: Dict[str, Any]):
        user_db: UserDB = UserDB.get_first({"id": userinfo["id"]})
        if user_db:
            user_db.delete()
            return True
        return False
    
    @classmethod
    def get_user_by_id(cls, userinfo: Dict[str, Any]):
        user_db: UserDB = UserDB.get_first({"id": userinfo["id"]})
        if user_db:
            return cls.instance_creator(user_db)
        return None

    @classmethod
    def get_user_by_username(cls, userinfo: Dict[str, Any]):
        user_db: UserDB = UserDB.get_first({"username": userinfo["username"]})
        if user_db:
            return cls.instance_creator(user_db)
        return None
    
    @classmethod
    def get_user_by_email(cls, userinfo: Dict[str, Any]):
        user_db: UserDB = UserDB.get_first({"email": userinfo["email"]})
        if user_db:
            return cls.instance_creator(user_db)
        return None
    
    @classmethod
    def get_posts(cls, userinfo: Dict[str, Any]):
        user_db: UserDB = UserDB.get_first({"id": userinfo["id"]})
        if user_db:
            return tuple([post.id for post in user_db.posts])
        return None
    
    @classmethod
    def get_followed(cls, userinfo: Dict[str, Any]):
        user_db: UserDB = UserDB.get_first({"id": userinfo["id"]})
        if user_db:
            return tuple([user.followed_id for user in user_db.followed])
        return None
    
    @classmethod
    def get_followers(cls, userinfo: Dict[str, Any]):
        user_db: UserDB = UserDB.get_first({"id": userinfo["id"]})
        if user_db:
            return tuple([user.follower_id for user in user_db.followers])
        return None
    
    @classmethod
    def get_likes(cls, userinfo: Dict[str, Any]):
        user_db: UserDB = UserDB.get_first({"id": userinfo["id"]})
        if user_db:
            return tuple([like.postid for like in user_db.likes])
        return None
    
    @classmethod
    def get_comments(cls, userinfo: Dict[str, Any]):
        user_db: UserDB = UserDB.get_first({"id": userinfo["id"]})
        if user_db:
            return tuple([comment.id for comment in user_db.comments])
        return None