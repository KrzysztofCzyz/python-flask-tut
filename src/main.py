from flask import Flask,render_template, url_for
from form import RegistrationForm, LoginForm
app= Flask(__name__)

app.config['SECRET_KEY'] = 'ef3f32aab117166afda5b61a27af21c7'

posts = [
    {
        'author': 'Me',
        'title': 'Blog Post 1',
        'content': 'Lorem ipsum...',
        'date_posted': 'April 21, 2018'
    },
    {
        'author': 'Me',
        'title': 'Blog Post 2',
        'content': 'Lorem ipsum...',
        'date_posted': 'April 22, 2018'
    }

]


@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title="About")


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)

