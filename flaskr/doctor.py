import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
from db_creation import * 
from db_insertion import *
from db_queries import *
from db_deletes import *


bp = Blueprint('doctor', __name__, url_prefix='/doctor')

@bp.route('/dashboard/<username>', methods=("GET", "POST"))
def doctors_dashboard(username):
    details = get_doctor_details(username)
    quals = get_doctor_qualifications(username)
    return render_template("doctors_about.html", username=username, name="Basics", details=details, quals=quals)

@bp.route('/appointments/<username>/<number>', methods=("GET", "POST"))
def doctors_appointments(username,number):
    aps = get_appointments(get_doctor_id(username))

    if request.method=="POST":
        button_key = 'button#'+str(number)
        val = request.form[button_key]
        delete_appointment(int(number))
        print('deleted',number)
        if val == "cancel":
            aps.remove(aps[int(number)-1])
            return render_template("doctors_appointments.html", number=0, username=username, aps=aps)
        else:
            aps.remove(aps[int(number)-1])
            return redirect(url_for(".doctors_pres", number=int(number)-1))

        # return render_template("doctors_appointments.html", number=int(number)-1, username=username, aps=aps)

    if request.method=='GET':
        return render_template("doctors_appointments.html", number=int(number)-1, username=username, aps=aps)

@bp.route('/about/<username>/<name>', methods=("GET", "POST"))
def doctors_about(username, name):
    docid = get_doctor_id(username)[0]
    details = get_doctor_details(username)
    quals = get_doctor_qualifications(username)
    specs = get_all_specs()
    slots = get_all_slots()
    docslots = get_doctor_slots(docid)
    docspecs = get_doctor_specs(docid)
    qual_det_list = get_doctor_qualifications(username)
    docquals = []
    for qual in qual_det_list:
        docquals.append(qual[0])

    if request.method=="POST":
        print(request.form)
        if "Specialization" in request.form:
            doc_specs = request.form.getlist("profiles")
            # print(specs)
            doctor_id = get_doctor_id(username)[0]
            print(docspecs)
            for spec in doc_specs:
                # print(spec, type(spec), get_spec_id(spec))
                if spec not in docspecs:
                    insert_specialized(get_spec_id(spec), doctor_id)
                    docspecs.append(spec)

            print(doc_specs)

            return render_template("doctors_about.html", username=username, name=name, details=details, quals=quals, docquals=docquals, specs=specs, docspecs=doc_specs, slots=slots, docslots=docslots)


        elif "Qualification" in request.form:
            institute = request.form['institute']
            procurement_year = request.form['year'][:4]
            qualifications = request.form.getlist('profiles')
            doctor_id = get_doctor_id(username)[0]
            
            for qual in qualifications:
                qual_id = get_qual_id(qual)
                if qual not in docquals:
                    insert_qualified(qual_id, doctor_id, procurement_year, institute)
                    docquals.append(qual)

            return render_template("doctors_about.html", username=username, name=name, details=details, quals=quals, docquals=docquals, specs=specs, docspecs=docspecs, slots=slots, docslots=docslots)
        
        else:
            # Reviewed
            start = request.form['start_time']
            end = request.form['end_time']

            # print(start,end)
            # print(docslots)
            timeslot = (datetime.strptime(start, '%H:%M'), datetime.strptime(end, '%H:%M'))
            
            slot = (start,end)

            if timeslot not in slots:
                insert_slot(start, end)
            
            if timeslot not in docslots:
                insert_has_slot(get_slot_id(slot), get_doctor_id(username))

            # for slot in slots:
            #     print(get_slot_id(slot))
            #     insert_has_slot(get_slot_id(slot), get_doctor_id(username))
            docslots = get_doctor_slots(docid)

            return render_template("doctors_about.html", username=username, name=name, details=details, quals=quals, docquals=docquals, specs=specs, docspecs=docspecs, slots=slots, docslots=docslots)
    
    if request.method=="GET":
        
        return render_template("doctors_about.html", username=username, name=name, details=details, quals=quals, docquals=docquals, specs=specs, docspecs=docspecs, slots=slots, docslots=docslots)

@bp.route('/prescription/<number>', methods=("GET", "POST"))
def doctors_pres(number):
    return render_template("prescription.html", number=number)