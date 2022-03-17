#!/usr/bin/python

import psycopg2
from config import config


def search_patient(username, password):
    signed_up = 0
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        sql = "SELECT username, password FROM patient where username=%s and password=%s;"
        cur.execute(sql, (username, password))
        
        if cur.rowcount > 0:
            signed_up = 1
        
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return signed_up


def search_doctor(username, password):
    signed_up = 0
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        sql = "SELECT username, password FROM doctor where username=%s and password=%s;"
        cur.execute(sql, (username, password))
        
        if cur.rowcount > 0:
            signed_up = 1
        
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return signed_up


def search_username(username):
    signed_up = 0
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        sql = "SELECT username, password FROM patient where username=%s;"
        cur.execute(sql, (username,))
        
        if cur.rowcount > 0:
            signed_up = 1

        sql = "SELECT username, password FROM doctor where username=%s;"
        cur.execute(sql, (username,))

        if cur.rowcount > 0:
            signed_up = 1
        
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return signed_up


def search_spec_id(speciality):
    spec_id = -1
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        sql = "SELECT spec_id FROM specialization where speciality=%s;"
        cur.execute(sql, (speciality,))
        spec_id = cur.fetchone()[0]      
        
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return spec_id


def search_qual_id(qual_name):
    qual_id = -1
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        sql = "SELECT qual_id FROM qualification where qual_name=%s;"
        cur.execute(sql, (qual_name,))
        qual_id = cur.fetchone()[0]      
        
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return qual_id


def get_history(patient_id):
    conn = None
    hist = []
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        sql = """
        SELECT a.appointment_date, a.appointment_time, d.name FROM history h 
        left join appointments a on a.patient_id=h.patient_id 
        left join doctor d on d.doctor_id=a.doctor_id
        where h.patient_id=%s;
        """

        cur.execute(sql, (patient_id, ))

        for i in range(cur.rowcount):
            hist.append(cur.fetchone())
        
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return hist    


def get_appointments(doctor_id):
    conn = None
    appts = []
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        sql = """
        SELECT a.appointment_date, a.appointment_time, p.name FROM appointments a 
        left join patient p on p.patient_id=a.patient_id 
        where a.doctor_id=%s;
        """

        cur.execute(sql, (doctor_id, ))

        for i in range(cur.rowcount):
            appts.append(cur.fetchone())
        
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return appts  

