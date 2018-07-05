# Radio, Select and SelectMultiple

# simple web form component
from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from wtforms import (
    RadioField, SelectField, SelectMultipleField, SubmitField, validators
)

app = Flask(__name__)
app.secret_key = 'jiaqixu'

class ContactForm(FlaskForm):
    radio = RadioField('please select one', choices=[('value_1', 'choice_1'), ('value_2', 'choice_2'), ('value_3', 'choice_3')],
    validators=[validators.AnyOf(['value_1', 'value_2', 'value_3'], 'please select one value')])

    select = SelectField('please select a day', choices=[('monday', 'Mon.'), ('tuesday', 'Tues.'), ('wednsday', 'Wed.'),
    ('thursday', 'Thurs.'), ('friday', 'Fri.'), ('saturday', 'Sat.'), ('sunday', 'Sun.')],
    validators=[validators.AnyOf(['tuesday'], 'please select Tuesday')])

    selectMultiple = SelectMultipleField('please select mutiple items', choices=[('value_1', 'choice_1'), ('value_2', 'choice_2'), ('value_3', 'choice_3')],
    validators=[validators.AnyOf([['value_1', 'value_2'], ['value_1', 'value_3']], 'only choose the top 2 items or the first and third item')])
    submit = SubmitField('submit')


@app.route('/', methods=['GET','POST'])
def contact():
    form = ContactForm()
    ok = False
    if request.method == 'POST':
        if form.validate_on_submit()==False:
            print('error')
        else:
            print('input successfully')
            ok = True
    return render_template('select.html', form = form, ok = ok)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
