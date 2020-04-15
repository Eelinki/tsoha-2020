from application import db
from application.models import Base

class Board(Base):
    boardname = db.Column(db.String(64), nullable=False)

    threads = db.relationship("Thread", backref='threads', lazy=True)

    def __init__(self, boardname):
        self.boardname = boardname