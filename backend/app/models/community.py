from app.models import db
from datetime import datetime, timezone


# Association table for M:N (users & communities)
community_members = db.Table(
    "community_members",
    db.Column("user_id", db.Integer, db.ForeignKey("users.id"), primary_key=True),
    db.Column("community_id", db.Integer, db.ForeignKey("communities.id"), primary_key=True),
    db.Column("joined_at", db.DateTime(timezone=True), server_default=db.func.now())
)


class Community(db.Model):
    __tablename__ = "communities"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False, index=True)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(120), nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=db.func.now())

    # Relationships
    members = db.relationship(
        "User",
        secondary=community_members,
        back_populates="communities"
    )
    posts = db.relationship(
        "Post",
        back_populates="community",
        lazy=True,
        cascade="all, delete-orphan"
    )
    events = db.relationship(
        "Event",
        back_populates="community",
        lazy=True,
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Community {self.name}>"
