from application import db
from application.models import Base

group_users = db.Table(
    'group_users',
    db.Column('group_id', db.Integer, db.ForeignKey('group.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('account.id'))
)

class Group(Base):
    groupname = db.Column(db.String(64), nullable=False)

    def __init__(self, groupname):
        self.groupname = groupname