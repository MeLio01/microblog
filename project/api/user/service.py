from typing import Dict, Any

from .interface import User

from project.api.post import Post

def get_likes_by_user(userinfo: Dict[str, Any]):
    posts_id = User.get_likes(userinfo)
    if posts_id:
        posts = []
        for post_id in posts_id:
            post = Post.post_by_id({"id": post_id})
            posts.append({
                "id": post.id,
                "body": post.body
            })
        return posts
    return None

def get_posts_by_user(userinfo: Dict[str, Any]):
    posts_id = User.get_posts(userinfo)
    if posts_id:
        posts = []
        for post_id in posts_id:
            post = Post.post_by_id({"id": post_id})
            posts.append({
                "id": post.id,
                "body": post.body
            })
        return posts
    return None