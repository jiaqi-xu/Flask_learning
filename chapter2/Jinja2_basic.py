# Jinja2 pattern basic

# Web pattern = Html page(js, css, html) + dynamic part

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name= name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
