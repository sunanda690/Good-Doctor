import os

from flask import Flask
from flask import render_template, request
from models import create_patient_table, insert_signup_info, search_patient

create_patient_table()

app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
)

# a simple page that says hello
@app.route('/signup', methods=('GET', 'POST'))
def signup():
    if request.method == 'GET':
        return render_template("signup.html")

    else:
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        insert_signup_info(username, email, password)
        return render_template("signin.html")


@app.route('/signin', methods=('GET', 'POST'))
def signin():
    if request.method == 'GET':
        return render_template("signin.html")

    else:
        username = request.form['username']
        password = request.form['password']

        if search_patient(username, password):
            return render_template("index.html")

        else:
            return render_template("signin.html")


@app.route('/index', methods=('GET', 'POST'))
def index():
    if request.method == 'GET':
        return render_template("index.html")
