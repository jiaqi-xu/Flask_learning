# WTFrom Validation functions
from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from wtforms import (
    TextField, IntegerField, PasswordField, RadioField, TextAreaField, BooleanField,
    DateField, SubmitField, validators
)

app = Flask(__name__)
app.secret_key = 'jiaqixu'


class MyForm(FlaskForm):
    name = TextField('name', [validators.Required('please type your name')])
    email = TextField('e-mail', [validators.Required('please type your email'),validators.Email('please type right email format')])
    ip = TextField('ip', [validators.IPAddress(message='please type correct ip address')])
    password_1 = PasswordField('password', [validators.Required('please type password')])
    password_2 = PasswordField('password again', [validators.Required('please type password again'), validators.EqualTo('password_1', 'password not consistent')])

    url = TextField('Url', [validators.URL('wrong format'), validators.optional()])
    regexpValue = TextField('regex_expression', [validators.Regexp('^[a-z]{3}-[1-9]{3}$', message='correct format should be abc-123'), validators.optional()])
    submit = SubmitField('submit')


@app.route('/', methods=['GET','POST'])
def contact():
    form = MyForm()
    ok = False
    if request.method == 'POST':
        if form.validate_on_submit() == False:
            print('error')
        else:
            print('validation successfully')
            ok = True
    return render_template('validation.html', form = form, ok = ok)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
