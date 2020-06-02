from flask import Flask, escape, request

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def hello():
    name = request.args.get("name", "World")
    return f'<h1>Home page</h1>'


@app.route('/about')
def about():
    name = request.args.get("name", "World")
    return f'<h1>About Page</h1>'


# This condition is only true if we run the script directly
# This helps avoid using environment variables
# This way you can run the app by using 'python flaskblog.py'
if __name__ == '__main__':
    app.run(debug=True)
