from app.models import db
from datetime import datetime, timezone


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(255), nullable=True)
    post_type = db.Column(db.String(50), nullable=False, index=True, default="post")
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=db.func.now())

    # Foreign Keys
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, index=True)
    community_id = db.Column(db.Integer, db.ForeignKey("communities.id"), nullable=True, index=True)

    # Relationships
    author = db.relationship("User", back_populates="posts")
    community = db.relationship("Community", back_populates="posts")

    def __repr__(self):
        return f"<Post {self.title} ({self.post_type})>"
