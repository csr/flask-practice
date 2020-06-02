from flask import Flask, escape, request, render_template, url_for

app = Flask(__name__)

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
def hello():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


# This condition is only true if we run the script directly
# This helps avoid using environment variables
# This way you can run the app by using 'python flaskblog.py'
if __name__ == '__main__':
    app.run(debug=True)
