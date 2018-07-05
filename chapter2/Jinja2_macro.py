# Jinja2 pattern condition control
from flask import Flask, render_template

app = Flask(__name__)


class MyItem:
    def __init__(self, id, name):
        self.id = id
        self.name = name


@app.route('/')
def index():
    return render_template('macro.html',
    items=[{'id':1, 'name': 'Mike'}, {'id':2, 'name': 'Jay'}, MyItem(3, 'Jam')])


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
