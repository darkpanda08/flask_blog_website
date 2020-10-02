from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'John Doe',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'August 20, 2020'
    },
    {
        'author': 'Mark Abyy',
        'title': 'Blog Post 2',
        'content': 'Secong Post Content',
        'date_posted': 'August 22, 2020'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts, title='Home')

@app.route("/about")
def about():
    return render_template('about.html', title='About')