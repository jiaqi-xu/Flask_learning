# Jinja2 pattern custom error page
'''
404: not found
505: internal error
'''
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/500')
def index():
    raise Exception('internal error, please check your code')

    return render_template('error.html', name='jq')


@app.errorhandler(404)
def page_not_found(e):
    print e
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html', error=e), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
