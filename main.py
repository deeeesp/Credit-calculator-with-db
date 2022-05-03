import os
import re

import base.base
from models.condition import Condition
from models.bank import Bank
from flask import Flask, render_template, request
from models.database import DATABASE_NAME, Session
import create_database as db_creator
import bank_interest as bank_interest

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    session = Session()
    a = []
    if request.method == 'POST':
        if request.form.get('type') is not None:
            t, pr, pe = request.form.get('type').split(';')
            b = bank_interest.BankInterest(int(request.form.get('sum')), int(pe),
                                           int(pr))
            if t == 'differentiable':
                plata, result = b.diff_int()
                l = []
                for i in range(len(plata)):
                    l.append("Выплата на " + str(i + 1) + " месяц = " + str(plata[i]))
                return render_template('index.html', count=result, plata=l)
            else:
                l, result = b.ann_int()
                return render_template('index.html', count=result, d=str(l))
        else:
            bank = request.form.get('bank')
            bank = ''.join(char for char in bank if char.isalnum())
            for i in session.query(Bank.id).filter(Bank.title == bank):
                a = i
            return render_template('index.html', bank_value=bank,
                                   payment_type_base=session.query(Condition).filter(
                                       Condition.bank_id == a[0] - 1))
    else:
        return render_template('index.html', banks_base=session.query(Bank.title))


if __name__ == "__main__":
    session = Session()
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()
    app.run()
