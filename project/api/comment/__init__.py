from .model import Comment as CommentDB
from .interface import Comment
from .controller import comment_blueprint
from .schema import comment_id_schema, comment_out_schema, comment_schema