from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .post import Post
from .event import Event
from .report import Report
from .community import Community

__all__ = ['db', 'User', 'Post', 'Event', 'Report', 'Community']
