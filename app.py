from flask import Flask, render_template

flask_app = Flask(__name__)

@flask_app.route('/')
def homepage():
    f = open('goods.txt', 'r', encoding='utf-8')
    txt = f.readlines()
    return render_template('index.html', goods=txt)

