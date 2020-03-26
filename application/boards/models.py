from application import db

class Board(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    boardname = db.Column(db.String(64), nullable=False)

    def __init__(self, boardname):
        self.boardname = boardname