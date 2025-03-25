from flask import render_template, redirect, url_for, request
from app import app

posts = []

@app.route('/')
def index():
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
