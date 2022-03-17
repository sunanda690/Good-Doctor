import os

from flask import Flask
from flask import render_template, request, redirect, url_for
# from database import create_patient_table, insert_signup_info, search_patient
from . import doctor
from db_creation import * 
from db_insertion import *
from db_queries import *

create_patient_table()
create_doctor_table()


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


@app.route('/patients_dashboard/<username>', methods=('GET', 'POST'))
def patients_dashboard(username):
    if request.method == 'POST':
        appointmentDate = request.form['date']
        symptoms = request.form['symptom']
        
        print("{} {}".format(appointmentDate, symptoms))

    symptoms = ["Fever", "Stomachache", "Headache", "Cough"]
    return render_template("patients_dashboard.html", symptoms=symptoms)


@app.route('/patients_signup.html', methods=('GET', 'POST'))
def patients_signup():
    if request.method == 'GET':
        return render_template("patients_signup.html")

    else:
        username = request.form['username']
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        age = request.form['age']
        mobile_number = request.form['mobile_number']
        
        if search_username(username)==1:
            return render_template("patients_signup.html")

        insert_patient(username, name, email, password, mobile_number, age)
        return render_template("patients_signin.html")


@app.route('/doctors_signup.html', methods=('GET', 'POST'))
def doctors_signup():
    if request.method == 'GET':
        return render_template("doctors_signup.html")

    else:
        username = request.form['username']
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        age = request.form['age']
        experience = request.form['experience']
        mobile_number = request.form['mobile_number']

        if search_username(username)==1:
            return render_template("doctors_signup.html")

        insert_doctor(username, name, email, password, mobile_number, age, experience)
        return render_template("doctors_signin.html")

@app.route('/patient_profile.html', methods=('GET', 'POST'))
def patients_profile():
    if request.method == 'GET':
        return render_template("patient_profile.html")

@app.route('/patients_signin.html', methods=('GET', 'POST'))
def patients_signin():
    if request.method == 'GET':
        return render_template("patients_signin.html")

    else:
        username = request.form['username']
        password = request.form['password']

        if search_patient(username, password):
            return render_template("patients_dashboard.html", username=username)

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