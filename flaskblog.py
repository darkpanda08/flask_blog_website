from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '2d4fc582abd6ceeb0c8045f58f06c882'

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

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for { form.username.data }!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Login Unsuccessful. Please check username and passowrd', 'danger')
    
    return render_template('login.html', title='Login', form=form)