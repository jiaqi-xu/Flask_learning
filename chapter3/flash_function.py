# use flash function send message to client
from flask import Flask, request, render_template, flash
from flask_wtf import FlaskForm
from wtforms import (
    TextField, IntegerField, TextAreaField, BooleanField,
    DateField, SubmitField, validators
)

app = Flask(__name__)
app.secret_key = 'jiaqixu'

class ContactForm(FlaskForm):
    name = TextField('name', [validators.Required('name is required')])
    age = IntegerField(
                'age', [validators.Required('age is required'),
                validators.NumberRange(10, 30, 'age must between 10 ~ 30')]
            )
    birth = DateField('birth_date', [validators.Required('birth date is required')])
    isStudent= BooleanField('is student')
    resume = TextAreaField('resume', [validators.Length(10, 200, 'resume length must between 10 ~ 200')])
    submit = SubmitField('submit')


@app.route('/', methods=['GET','POST'])
def contact():
    form = ContactForm()
    ok = False
    if request.method == 'POST':
        if form.validate_on_submit()==False:
            print('error')
        else:
            flash('input successfully')
            flash('<h2>jiaqixu</h2>')
            print('input successfully')
            ok = True
    return render_template('flash.html', form = form, ok = ok)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
