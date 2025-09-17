from app.models import db
from datetime import datetime
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    bio = db.Column(db.Text, nullable=True)
    location = db.Column(db.String(120), nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    # Relationships
    posts = db.relationship("Post", backref="author", lazy=True, cascade="all, delete-orphan")
    reports = db.relationship("Report", backref="reporter", lazy=True, cascade="all, delete-orphan")
    events = db.relationship("Event", backref="organizer", lazy=True, cascade="all, delete-orphan")
    communities = db.relationship("Community", secondary="community_members", back_populates="members")

    # Password methods
    def set_password(self, password):
        """Hashes and sets the user's password."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Verifies the provided password against the stored hash."""
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.username}>"
