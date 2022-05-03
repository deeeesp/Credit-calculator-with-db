import random

from models.database import create_db, Session
from models.bank import Bank
from models.condition import Condition


def create_database(load_fake_data: bool = True):
    create_db()
    if load_fake_data:
        _load_fake_data(Session())


def _load_fake_data(session: Session):
    b1 = Bank(title='Тинькофф')
    b2 = Bank(title='Сбербанк')
    b3 = Bank(title='Альфабанк')
    session.add(b1)
    session.add(b2)
    session.add(b3)
    cond_type = ['annuities', 'differentiable']
    banks = [b1, b2, b3]
    for _ in range(30):
        bank_id = random.randint(0, len(banks) - 1)
        payment_type = random.choice(cond_type)
        period = random.randint(1, 10)
        percent = random.randint(11, 20)
        condition = Condition(payment_type, percent, period, bank_id)
        session.add(condition)

    session.commit()
    session.close()
