from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from models.database import Base


class Bank(Base):
    __tablename__ = 'bank'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    condition = relationship('Condition')

    # group = Column(Integer, ForeignKey('groups.id'))

    def __repr__(self):
        return f'Банк [ID: {self.id}, Название: {self.title}]'

    def get_id(self):
        return int(self.id)
