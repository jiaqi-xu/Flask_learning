# Web Form and Flask-WTF extension
# 01-Form Class
'''
<form>

</form>
usage of Flask-WTF
1. generate web form component HTML code
2. back stage validation
3. return error info to web point 
4. return error info in web page
5. against domain-cross access
'''
from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField, validators

app = Flask(__name__)
app.secret_key = 'jiaqixu'

class ContactForm(FlaskForm):
    firstname = TextField('name', [validators.Required('name is required')])
    submit = SubmitField('submit')

@app.route('/', methods=['GET','POST'])
def contact():
    form = ContactForm()
    print(form.firstname)
    print(form.firstname.label)
    if request.method == 'POST':
        if form.validate_on_submit()==False:
            print(form.firstname.errors)
            print "error"
    return render_template('first.html', form = form)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
