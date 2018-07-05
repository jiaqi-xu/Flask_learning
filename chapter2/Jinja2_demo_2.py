# Jinja2 pattern filter
from flask import Flask, render_template
'''
Jinja2 support filters:
safe: 渲染值时不转义
capitalize: 把值的首字母转换成大写，其他字母转换成小写
lower: 把值的所有字母都换成小写
upper: 把值的所有字母都换成大写
title: 把每个单词的首字母都换成大写
trim: 把值的首尾空格去掉
striptags: 渲染之前将值中所有的HTMl标签去掉
'''
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('filter.html', name='bill', value='<h1>hello</h1>')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
