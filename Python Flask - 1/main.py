from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__, template_folder='templates')
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contact/')
def contact():
    return render_template('contact.html')


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/login/')
def login():
    return render_template('login.html')


@app.route('/register/')
def register():
    return render_template('register.html')


@app.errorhandler(404)
def page_error(e):
    return render_template('error.html')


if __name__ == '__main__':
    app.run(debug=True)
