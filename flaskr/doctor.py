import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash


bp = Blueprint('doctor', __name__, url_prefix='/doctor')

@bp.route('/dashboard', methods=("GET", "POST"))
def doctors_dashboard():
    return render_template("doctors_about.html", name="Basics")

@bp.route('/appointments/<number>', methods=("GET", "POST"))
def doctors_appointments(number):
    if request.method=="POST":
        num = int(request.form.keys()[0].split("#"))
        if request.form["button#{}".format(num)] == "cancel":
            render_template("doctors_appointments.html", number=1)
        else:
            redirect(url_for(".doctors_pres", number=num))
    return render_template("doctors_appointments.html", number=number)

@bp.route('/about/<name>', methods=("GET", "POST"))
def doctors_about(name):
    if request.method=="POST":
        if "Specialization" in request.form:
            specs = request.form['profiles']
        elif "Qualification" in request.form:
            name = request.form['institute']
            year = request.form['year']
        else:
            slots = request.form['slots']
    return render_template("doctors_about.html", name=name)

@bp.route('/prescription/<number>', methods=("GET", "POST"))
def doctors_pres(number):
    return render_template("prescription.html", number=number)