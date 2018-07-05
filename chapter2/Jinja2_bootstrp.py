# use Flask_bootstrap integrate Twitter Bootstrp
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('bs.html', name='jq')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
