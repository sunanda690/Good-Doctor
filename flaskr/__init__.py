import os

from flask import Flask
from flask import render_template, request, redirect, url_for
# from database import create_patient_table, insert_signup_info, search_patient
from . import doctor
from db_creation import * 
from db_insertion import *
from db_queries import *

# create_patient_table()
# create_doctor_table()


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
        appointmentDate = str(request.form['date'])
        appointmentPrefferedtime = str(request.form['time'])
        symptoms = request.form['symptom']
        
        print("{} {}".format(appointmentDate, symptoms))

        patid = get_patient_id(username)
        appointment = get_best_doctor([symptoms], str(appointmentPrefferedtime))
        docid = appointment[0]
        endtime = appointment[1][1]
        starttime = str(appointment[1][0])
        insert_appointment(appointmentDate, starttime, patid, docid)
    symptoms = get_all_symptoms()
    details = get_patient_details(username)
    return render_template("patients_dashboard.html", symptoms=symptoms, username=username, details=details)


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
        return redirect(url_for("patients_signin"))


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
        return redirect(url_for("doctors_signin"))

@app.route('/patient_profile/<username>/<name>', methods=('GET', 'POST'))
def patients_profile(username, name):
    if request.method == 'GET':
        details = get_patient_details(username)
        history = get_history(details['patient_id'])
        return render_template("patient_profile.html",username=username,name=name, details=details, history=history)

@app.route('/patients_signin', methods=('GET', 'POST'))
def patients_signin():
    if request.method == 'GET':
        return render_template("patients_signin.html")

    else:
        username = request.form['username']
        password = request.form['password']
        

        if search_patient(username, password):
            return redirect(url_for("patients_dashboard", username=username))

        else:
            return render_template("patients_signin.html")


@app.route('/doctors_signin', methods=('GET', 'POST'))
def doctors_signin():
    if request.method == 'GET':
        return render_template("doctors_signin.html")

    else:
        username = request.form['username']
        password = request.form['password']
        print("{} {}", username, password, search_doctor(username, password))
        if search_doctor(username, password):
            return redirect(url_for("doctor.doctors_dashboard", username=username))

        else:
            return redirect(url_for("doctors_signin"))



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