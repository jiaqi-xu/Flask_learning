# Jinja2 pattern using complex data
from flask import Flask, render_template

app = Flask(__name__)


class MyClass:
    def func(self):
        return 'func'


def myFunc():
    return 'myFunc'


@app.route('/')
def index():
    mydict = {}
    mydict['type'] = 'dict'
    mylist = []
    mylist.append('list')
    myclass = MyClass()
    return render_template(
        'template.html', mydict=mydict, mylist=mylist,
        myclass=myclass, myfunc=myFunc)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
