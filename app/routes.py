from flask import render_template, redirect, url_for, request
from app import app

posts = []
userinfo = {}
@app.route('/')
def mainpage():
    return render_template('index.html')

@app.route('/blog/', methods=['GET', 'POST'])
def blog():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']
        if title and text:
            posts.append({'title': title, 'text': text})
        return redirect(url_for('blog'))
    return render_template('blog.html', posts=posts)

@app.route('/user/', methods=['GET', 'POST'])
def user():
    if request.method == 'POST':
        userinfo["name"] = request.form['name']
        userinfo["address"] = request.form['address']
        userinfo["hobby"] = request.form['hobby']
        userinfo["age"] = request.form['age']
        return redirect(url_for('user'))
    return render_template('user.html', user=userinfo)

@app.route('/user/edit')
def user_edit():
    if userinfo=={}:
        return redirect(url_for('user'))
    return render_template('user_edit.html', user=userinfo)
