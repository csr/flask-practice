from flask import Flask, escape, request, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '93590f0e3dc7099d1f75f2607779ad4f'

posts = [
    {
        'auhtor': 'Cesare de Cal',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'June 1st',
    },
    {
        'auhtor': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'June 2nd',
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


# This condition is only true if we run the script directly
# This helps avoid using environment variables
# This way you can run the app by using 'python flaskblog.py'
if __name__ == '__main__':
    app.run(debug=True)
