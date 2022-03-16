#!/usr/bin/python

import psycopg2
from config import config


def insert_patient(username, name, email, password, mobile_number, age):
    """ insert a new vendor into the vendors table """
    sql = """INSERT INTO patient(username, name, email, password, mobile_number, age)
             VALUES(%s, %s, %s, %s, %s, %s) RETURNING patient_id, username, name, email, password, mobile_number, age;"""
    conn = None
    patient_id = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (username, name, email, password, mobile_number, age))
        # get the generated id back
        patient_details = cur.fetchone()
        # commit the changes to the database
        conn.commit()
        print(patient_details,"inserted")
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return patient_details


def insert_doctor(username, name, email, password, mobile_number, age, experience):
    """ insert a new vendor into the vendors table """
    sql = """INSERT INTO doctor(username, name, email, password, mobile_number, age, experience)
             VALUES(%s, %s, %s, %s, %s, %s, %s) RETURNING doctor_id, username, name, email, password, mobile_number, age, experience;"""
    conn = None

    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (username, name, email, password, mobile_number, age, experience))
        # get the generated id back
        doctor_details = cur.fetchone()
        # commit the changes to the database
        conn.commit()
        print(doctor_details,"inserted")
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return doctor_details


def insert_specialization(speciality):

    sql = """INSERT INTO specialization(speciality)
             VALUES(%s) RETURNING spec_id, speciality;"""
    conn = None

    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (speciality,))
        # get the generated id back
        spec_details = cur.fetchone()
        # commit the changes to the database
        conn.commit()
        print(spec_details,"inserted")
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return spec_details


def insert_specialized(spec_id, doctor_id):

    sql = """INSERT INTO specialized(spec_id, doctor_id)
             VALUES(%s, %s) RETURNING spec_id, doctor_id;"""
    conn = None

    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (spec_id, doctor_id))
        # get the generated id back
        spec_details = cur.fetchone()
        # commit the changes to the database
        conn.commit()
        print(spec_details,"inserted")
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return spec_details


def insert_qualification(qual_name):

    sql = """INSERT INTO qualification(qual_name)
             VALUES(%s) RETURNING qual_id, qual_name;"""
    conn = None

    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (qual_name,))
        # get the generated id back
        qual_details = cur.fetchone()
        # commit the changes to the database
        conn.commit()
        print(qual_details,"inserted")
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return qual_details


def insert_qualified(qual_id, doctor_id, procurement_year, institute):

    sql = """INSERT INTO qualified(qual_id, doctor_id, procurement_year, institute)
             VALUES(%s, %s, %s, %s) RETURNING qual_id, doctor_id, procurement_year, institute;"""
    conn = None

    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (qual_id, doctor_id, procurement_year, institute))
        # get the generated id back
        qual_details = cur.fetchone()
        # commit the changes to the database
        conn.commit()
        print(qual_details,"inserted")
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return qual_details


def insert_slot(start_time, end_time):

    sql = """INSERT INTO slots(start_time, end_time)
             VALUES(%s, %s) RETURNING slot_id, start_time, end_time;"""
    conn = None

    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (start_time, end_time))
        # get the generated id back
        qual_details = cur.fetchone()
        # commit the changes to the database
        conn.commit()
        print(qual_details,"inserted")
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return qual_details


def insert_has_slot(slot_id, doctor_id):

    sql = """INSERT INTO has_slots(slot_id, doctor_id)
             VALUES(%s, %s) RETURNING slot_id, doctor_id;"""
    conn = None

    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (slot_id, doctor_id))
        # get the generated id back
        qual_details = cur.fetchone()
        # commit the changes to the database
        conn.commit()
        print(qual_details,"inserted")
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return qual_details


def insert_prescription(patient_id, doctor_id):

    sql = """INSERT INTO prescription(patient_id, doctor_id)
             VALUES(%s, %s) RETURNING pres_id, patient_id, doctor_id;"""
    conn = None

    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (patient_id, doctor_id))
        # get the generated id back
        qual_details = cur.fetchone()
        # commit the changes to the database
        conn.commit()
        print(qual_details,"inserted")
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return qual_details


def insert_symptom(name):

    sql = """INSERT INTO symptom(name)
             VALUES(%s) RETURNING symptom_id, name;"""
    conn = None

    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (name,))
        # get the generated id back
        qual_details = cur.fetchone()
        # commit the changes to the database
        conn.commit()
        print(qual_details,"inserted")
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return qual_details


def insert_has_symptom(patient_id, symptom_id):

    sql = """INSERT INTO has_symptom(patient_id, symptom_id)
             VALUES(%s, %s) RETURNING patient_id, symptom_id;"""
    conn = None

    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (patient_id, symptom_id))
        # get the generated id back
        qual_details = cur.fetchone()
        # commit the changes to the database
        conn.commit()
        print(qual_details,"inserted")
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return qual_details


def insert_appointment(app_date, app_time, patient_id, doctor_id):

    sql = """INSERT INTO appointments(appointment_date, appointment_time, patient_id, doctor_id)
             VALUES(%s, %s, %s, %s) RETURNING appointment_id, appointment_date, appointment_time, patient_id, doctor_id;"""
    conn = None

    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (app_date, app_time, patient_id, doctor_id))
        # get the generated id back
        qual_details = cur.fetchone()
        # commit the changes to the database
        conn.commit()
        print(qual_details,"inserted")
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return qual_details


def insert_history(appointment_id, patient_id):

    sql = """INSERT INTO history(appointment_id, patient_id)
             VALUES(%s, %s) RETURNING appointment_id, patient_id;"""
    conn = None

    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (appointment_id, patient_id))
        # get the generated id back
        qual_details = cur.fetchone()
        # commit the changes to the database
        conn.commit()
        print(qual_details,"inserted")
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return qual_details


def insert_medicine(medicine, pres_id):

    sql = """INSERT INTO pres_medicines(medicine, pres_id)
             VALUES(%s, %s) RETURNING medicine, pres_id;"""
    conn = None

    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (medicine, pres_id))
        # get the generated id back
        qual_details = cur.fetchone()
        # commit the changes to the database
        conn.commit()
        print(qual_details,"inserted")
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return qual_details


def insert_diagnosis(diagnosis, pres_id):

    sql = """INSERT INTO pres_diagnosis(diagnosis, pres_id)
             VALUES(%s, %s) RETURNING diagnosis, pres_id;"""
    conn = None

    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (diagnosis, pres_id))
        # get the generated id back
        qual_details = cur.fetchone()
        # commit the changes to the database
        conn.commit()
        print(qual_details,"inserted")
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return qual_details


def insert_test(test, pres_id):

    sql = """INSERT INTO pres_test(test, pres_id)
             VALUES(%s, %s) RETURNING test, pres_id;"""
    conn = None

    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (test, pres_id))
        # get the generated id back
        qual_details = cur.fetchone()
        # commit the changes to the database
        conn.commit()
        print(qual_details,"inserted")
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return qual_details


def insert_symptoms(symptoms, pres_id):

    sql = """INSERT INTO pres_symptoms(symptoms, pres_id)
             VALUES(%s, %s) RETURNING symptoms, pres_id;"""
    conn = None

    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (symptoms, pres_id))
        # get the generated id back
        qual_details = cur.fetchone()
        # commit the changes to the database
        conn.commit()
        print(qual_details,"inserted")
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return qual_details


def insert_payment(amount, appointment_id):

    sql = """INSERT INTO payments(amount, appointment_id)
             VALUES(%s, %s) RETURNING payment_id, amount, appointment_id;"""
    conn = None

    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (amount, appointment_id))
        # get the generated id back
        qual_details = cur.fetchone()
        # commit the changes to the database
        conn.commit()
        print(qual_details,"inserted")
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return qual_details

