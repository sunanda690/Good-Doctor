import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from db_creation import * 
from db_insertion import *
from db_queries import *


bp = Blueprint('doctor', __name__, url_prefix='/doctor')

@bp.route('/dashboard/<username>', methods=("GET", "POST"))
def doctors_dashboard(username):
    details = get_doctor_details(username)
    quals = get_doctor_qualifications(username)
    return render_template("doctors_about.html", username=username, name="Basics", details=details, quals=quals)

@bp.route('/appointments/<username>/<number>', methods=("GET", "POST"))
def doctors_appointments(username,number):
    if request.method=="POST":
        num = int(request.form.keys()[0].split("#"))
        if request.form["button#{}".format(num)] == "cancel":
            render_template("doctors_appointments.html", number=1)
        else:
            redirect(url_for(".doctors_pres", number=num))
    aps = get_appointments(get_doctor_id(username))
    print(aps)
    return render_template("doctors_appointments.html", number=number, username=username, aps=aps)

@bp.route('/about/<username>/<name>', methods=("GET", "POST"))
def doctors_about(username, name):
    if request.method=="POST":
        print(request.form)
        if "Specialization" in request.form:
            specs = request.form['profiles']
            doctor_id = get_doctor_id(username)
            for spec in specs:
                insert_specialized(get_spec_id(spec), doctor_id)
        elif "Qualification" in request.form:
            institute = request.form['institute']
            procurement_year = request.form['year']
            qualification = request.form['profiles'][0]
            qual_id = get_qual_id(qualification)
            doctor_id = get_doctor_id(username)
            insert_qualified(qual_id, doctor_id, procurement_year, institute)
        else:
            # Reviewed
            slots = eval(request.form['slots'])
            print(eval(slots))
            for slot in slots:
                print(get_slot_id(slot))
                insert_has_slot(get_slot_id(slot), get_doctor_id(username))
    details = get_doctor_details(username)
    quals = get_doctor_qualifications(username)
    specs = get_all_specs()
    slots = get_all_slots()
    docslots = get_doctor_slots(get_doctor_id(username))
    return render_template("doctors_about.html", username=username, name=name, details=details, quals=quals, specs=specs, slots=slots, docslots=docslots)

@bp.route('/prescription/<number>', methods=("GET", "POST"))
def doctors_pres(number):
    return render_template("prescription.html", number=number)