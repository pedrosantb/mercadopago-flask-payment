from flask import render_template, flash, redirect, request, url_for, jsonify, session
from app import app, db
from app.forms import PaymentForm
from sqlalchemy import update, create_engine

import os
import json

from app.models import Payments
from app.forms import PaymentForm

from dotenv import load_dotenv

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))
engine = create_engine(os.getenv('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db'))


@app.route('/', methods=['POST', 'GET'])
@app.route('/index/', methods=['POST', 'GET'])
def index():
    title = "Index page"
    form = PaymentForm()

    try:
        payments = Payments.query.all()
    except:
        payments = []

    if form.is_submitted():
        payment = Payments(value=form.value.data)
        db.session.add(payment)
        db.session.commit()
        flash('Payment Commited!')
        return redirect(url_for('index'))
    return render_template('index.html', title=title, form=form, payments=payments)

