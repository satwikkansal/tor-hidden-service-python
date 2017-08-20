import datetime
import random

from flask import render_template, redirect, request
from app import app

posts = []

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='Voice of the Internet!',
                           posts=posts)


@app.route('/submit', methods=['POST'])
def submit_textarea():
    post_content = request.form["text"]

    nickname = request.form["nick"]
    if not nickname:
        nickname = "Anon" + str(random.randint(100000, 999999))

    posts.insert(0,
                 {
                     'author': {'nickname': nickname},
                     'body': post_content,
                     'time': datetime.datetime.now().strftime('%H:%M:%S')
                 })

    return redirect('/index')
