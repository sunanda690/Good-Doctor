import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash


bp = Blueprint('doctor', __name__, url_prefix='/doctor')

@bp.route('/dashboard', methods=("GET", "POST"))
def doctors_dashboard():
    return render_template("doctors_dashboard.html")

@bp.route('/appointments/<number>', methods=("GET", "POST"))
def doctors_appointments(number):
    return render_template("doctors_appointments.html", number=number)

@bp.route('/about/<name>', methods=("GET", "POST"))
def doctors_about(name):
    return render_template("doctors_about.html", name=name)