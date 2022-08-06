from typing import Dict, Any

from .interface import User

from project.api.post import Post
from project.api.comment import Comment

def get_comments_by_user(userinfo: Dict[str, Any]):
    comments_id = User.get_comments(userinfo)
    if comments_id:
        comments = []
        for comment_id in comments_id:
            comment = Comment.get_comment({"id": comment_id})
            comments.append({
                "post_id": comment.postid,
                "comment_id": comment.id,
                "body": comment.body
            })
        return comments
    return None

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