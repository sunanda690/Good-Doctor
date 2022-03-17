import os

from flask import Flask
from flask import render_template, request, redirect, url_for
# from database import create_patient_table, insert_signup_info, search_patient
from . import doctor

# create_patient_table()

app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
)
app.register_blueprint(doctor.bp)

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'GET':
        return render_template("index.html")

@app.route('/index.html', methods=('GET', 'POST'))
def index_html():
    if request.method == 'GET':
        return render_template("index.html")


@app.route('/patients_dashboard.html', methods=('GET', 'POST'))
def patients_dashboard():
    if request.method == 'GET':
        return render_template("patients_dashboard.html")


@app.route('/patients_signup.html', methods=('GET', 'POST'))
def patients_signup():
    if request.method == 'GET':
        return render_template("patients_signup.html")

    else:
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        insert_signup_info(username, email, password)
        return render_template("patients_signin.html")


@app.route('/doctors_signup.html', methods=('GET', 'POST'))
def doctors_signup():
    if request.method == 'GET':
        return render_template("doctors_signup.html")

    else:
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        insert_signup_info(username, email, password)
        return render_template("doctors_signin.html")


@app.route('/patients_signin.html', methods=('GET', 'POST'))
def patients_signin():
    if request.method == 'GET':
        return render_template("patients_signin.html")

    else:
        username = request.form['username']
        password = request.form['password']

        if search_patient(username, password):
            return render_template("patients_dashboard.html")

        else:
            return render_template("patients_signin.html")


@app.route('/doctors_signin.html', methods=('GET', 'POST'))
def doctors_signin():
    if request.method == 'GET':
        return render_template("doctors_signin.html")

    else:
        username = request.form['username']
        password = request.form['password']

        if search_patient(username, password):
            return redirect(url_for("doctor.doctors_dashboard"))

        else:
            return render_template("patients_signin.html")



@app.route('/departments.html', methods=('GET', 'POST'))
def departments():
    if request.method == 'GET':
        return render_template("departments.html")


@app.route('/about.html', methods=('GET', 'POST'))
def about():
    if request.method == 'GET':
        return render_template("about.html")

@app.route('/contact.html', methods=('GET', 'POST'))
def contact():
    if request.method == 'GET':
        return render_template("contact.html")