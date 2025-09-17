from app.models import db
from datetime import datetime, timezone


class Event(db.Model):
    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    poster_url = db.Column(db.String(255), nullable=True)
    event_date = db.Column(db.Date, nullable=False)
    event_time = db.Column(db.Time, nullable=False)
    location = db.Column(db.String(200), nullable=False)
    registration_link = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=db.func.now())

    # Foreign Keys
    organizer_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, index=True)
    community_id = db.Column(db.Integer, db.ForeignKey("communities.id"), nullable=True, index=True)

    # Relationships
    organizer = db.relationship("User", back_populates="events")
    community = db.relationship("Community", back_populates="events")

    def __repr__(self):
        return f"<Event {self.title} on {self.event_date}>"
