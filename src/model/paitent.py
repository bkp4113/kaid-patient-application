from sqlalchemy import Column, Integer, String
from src.db.database import Base

class Patient(Base):

    id = Column('paitent_id', Integer, primary_key=True)
    first_name = Column('first_name', String(200))
    middle_name = Column('first_name', String(200))
    last_name = Column('first_name', String(200))
    dob = Column('first_name', String(10))
    gender = Column('first_name', String(10))

    def __init__(self, first_name, middle_name, last_name, dob, gender):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.dob = dob
        self.gender = gender

    def to_json(self):
        return dict(name=self.first_name)