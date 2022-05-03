from sqlalchemy import Column, Integer, String, ForeignKey

from models.database import Base


class Condition(Base):
    __tablename__ = 'condition'

    id = Column(Integer, primary_key=True)
    payment_type = Column(String)
    period = Column(Integer)
    percent = Column(Integer)
    bank_id = Column(Integer, ForeignKey('bank.id'))

    def __init__(self, payment_type: String, percent: int, period: int, bank_id: int):
        self.payment_type = payment_type
        self.period = period
        self.percent = percent
        self.bank_id = bank_id


    def __repr__(self):
        return str(self.payment_type) + ';' + str(self.period) + ';' + str(self.percent)
