from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Vineet',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Joe',
        'title': 'Blog Post 2',
        'content': 'Secong Post Content',
        'date_posted': 'April 22, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts, title='Home')

@app.route("/about")
def about():
    return render_template('about.html', title='About')