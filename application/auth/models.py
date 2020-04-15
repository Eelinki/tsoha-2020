from application import db
from application.models import Base

from sqlalchemy.sql import text

class User(Base):

    __tablename__ = "account"
    
    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    threads = db.relationship("Thread", backref='account', lazy=True)

    def __init__(self, username, password, name = ''):
        self.username = username
        self.password = password
        self.name = name
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        return ["ADMIN"]

    @staticmethod
    def users_without_threads():
        stmt = text("SELECT Account.id, Account.username FROM Account"
                     " LEFT JOIN Thread ON Thread.user_id = Account.id"
                     " GROUP BY Account.id"
                     " HAVING COUNT(Thread.id) = 0")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "username":row[1]})

        return response