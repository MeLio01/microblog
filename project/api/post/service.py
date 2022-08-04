from typing import Dict, Any

from .interface import Post

from project.api.user import User

def get_likes_on_post(postinfo: Dict[str, Any]):
    user_ids = Post.get_likes(postinfo)
    if user_ids:
        users = []
        for user_id in user_ids:
            user = User.get_user_by_id({"id": user_id})
            users.append({
                "id": user.id,
                "username": user.username
            })
        return users
    return None