from application import db
from application.models import Base

class Thread(Base):
    title = db.Column(db.String(64), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, title):
        self.title = title