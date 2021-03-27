from sqlalchemy import Column, Integer, String, inspect
from db.database import Base

class Patient(Base):

    __tablename__ = 'paitent'
    id = Column('id', Integer, primary_key=True)
    first_name = Column('first_name', String(200))
    middle_name = Column('middle_name', String(200))
    last_name = Column('last_name', String(200))
    dob = Column('dob', String(10))
    gender = Column('gender', String(10))

    def to_dict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }