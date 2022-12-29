from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import DataRequired, ValidationError, DataRequired, Email, EqualTo, Length, NumberRange


class PaymentForm(FlaskForm):
    value = DecimalField('Value', validators=[DataRequired()])
    submit = SubmitField('Add Payment')



    


