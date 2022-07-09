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


if __name__ == '__main__':
    app.run(debug=True)
