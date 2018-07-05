# Jinja2 pattern condition control
from flask import Flask, render_template
'''
Jinja2 pattern condition is False:
1. varialbe is not exsited
2. string is empty (length=0)
3. value is 0 or 0.0
4. empty list
5. empty dict
6. None
'''
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('if.html', user='bill', intValue=0.0,
                           list=[1,2,3], dict = {'a':'b'}, value=None)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
