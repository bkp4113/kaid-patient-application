from sqlalchemy import Column, Integer, String, inspect
from db.database import Base

class User(Base):

    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(64), index=True, unique=True)
    passwd = Column(String(128))
    role_id = Column(Integer)

    def to_dict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }

class Roles(Base):

    __tablename__ = 'roles'
    id = Column('id', Integer, primary_key=True)
    roles = Column('roles', String(10))

    def to_dict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }