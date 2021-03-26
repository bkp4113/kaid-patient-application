from sqlalchemy import Column, Integer, String
from src.db.database import Base

class User(Base):
    id = Column(Integer, primary_key=True)
    username = Column(String(64), index=True, unique=True)
    email = Column(String(120), index=True, unique=True)
    passwd = Column(String(128))
    role_id = Column(Integer(20))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def to_json(self):
        return dict(name=self.first_name)