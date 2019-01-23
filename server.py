from flask import Flask, render_template
from flask_json import FlaskJSON
from database import *

app = Flask(__name__)
FlaskJSON(app)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route('/email_confirmation/<token>')
def email_confirmation(token):
    # We use 'force' to skip mimetype checking to have shorter curl command.
    user = db_session.query(User).filter(User.token == token).first()
    return user.email


if __name__ == '__main__':
    app.run()
