from application import db
from application.models import Base

class Thread(Base):
    title = db.Column(db.String(64), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    board_id = db.Column(db.Integer, db.ForeignKey('board.id'), nullable=False)
    user = db.relationship("User", backref="threaduser", lazy=True)
    board = db.relationship("Board", backref="threadboard", lazy=True)

    def __init__(self, title):
        self.title = title