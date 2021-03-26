from sqlalchemy import Column, Integer, String
from src.db.database import Base

class Roles(Base):
    id = Column(Integer, primary_key=True)
    roles = Column(String(10))

    def __repr__(self):
        return '<Post {}>'.format(self.body)

    def to_json(self):
        return dict(name=self.first_name)