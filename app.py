from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """Default route that prints Hello CPS3500!"""
    return 'Hello CPS3500!'


@app.route('/new_page')
def new_page():
    """New page route that prints This is a New Page!"""
    return 'This is a New Page!'


@app.route('/user/<username>')
def user(username):
    """
    Render a template and pass the username variable.
    The template will detect if the username is 'jack'.
    """
    return render_template('user.html', username=username)


# Only include this block if you want to run app/app.py directly.
if __name__ == '__main__':
    app.run(debug=True)
