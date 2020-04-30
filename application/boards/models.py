from application import db
from application.models import Base

from sqlalchemy.sql import text

class Board(Base):
    boardname = db.Column(db.String(64), nullable=False)

    threads = db.relationship("Thread", backref='boardthreads', lazy=True, cascade="all, delete-orphan")

    def __init__(self, boardname):
        self.boardname = boardname
    
    @staticmethod
    def board_thread_count():
        stmt = text("SELECT Board.id, Board.boardname, COUNT(Thread.id) FROM Board"
                     " LEFT JOIN Thread ON Thread.board_id = Board.id"
                     " GROUP BY Board.id"
                     " ORDER BY -COUNT(Thread.id)")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "boardname":row[1], "threads":row[2]})

        return response