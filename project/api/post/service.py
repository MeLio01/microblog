from typing import Dict, Any

from .interface import Post

from project.api.user import User
from project.api.comment import Comment

def get_comments_on_post(postinfo: Dict[str, Any]):
    comment_ids = Post.get_comments(postinfo)
    if comment_ids:
        comments = []
        for comment_id in comment_ids:
            comment = Comment.get_comment({"id": comment_id})
            comments.append({
                "id": comment.id,
                "body": comment.body
            })
        return comments
    return None

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