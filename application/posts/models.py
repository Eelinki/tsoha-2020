from application import db
from application.models import Base

class Post(Base):
    message = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    thread_id = db.Column(db.Integer, db.ForeignKey('thread.id'), nullable=False)
    user = db.relationship("User", backref="postuser", lazy=True)

    def __init__(self, message):
        self.message = message