#!/usr/bin/python

import psycopg2
from config import config
from db_creation import *
from db_insertion import *

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


if __name__ == '__main__':
    create_patient_table()
    insert_patient("abhw", "abhilash", "abhi.com", "ajsb", "760", "21")
    insert_patient("ahw", "abhilash", "abhi.com", "ajsb", "760", "21")
    print(search_patient("ahw", "ajsb"))

    create_doctor_table()
    insert_doctor("abh", "abhilash", "abhi.com", "ajsb", "7602045111", "21", "3")
    insert_doctor("abhsad", "abhilash", "abhi.com", "ajsb", "7602045111", "21", "3")
    print(search_doctor("abhsad", "ajsb"))

    create_specialization_table()
    insert_specialization("cardio")
    insert_specialization("ENT")
    insert_specialization("Eye")
    print(search_spec_id("ENT"))

    create_specialized_table()
    insert_specialized(1,1)

    create_qualification_table()
    insert_qualification('MBBS')
    insert_qualification('MS')
    print(search_qual_id('MS'))

    create_qualified_table()
    insert_qualified(1,1,2020,'iitkgp')

    create_slots_table()
    insert_slot('03:00', '16:30')

    create_has_slots_table()
    insert_has_slot(1,1)

    create_prescription_table()
    insert_prescription(1,2)

    create_symptom_table()
    insert_symptom('cough')
    insert_symptom('cold')
    insert_symptom('congestion')

    create_has_symptom_table()
    insert_has_symptom(1,2)

    create_appointments_table()
    insert_appointment('3/15/2011', '12:33', 1, 1)

    create_history_table()
    insert_history(1,1)

    create_pres_medicines_table()
    insert_medicine('paracetamol', 1)

    create_pres_diagnosis_table()
    insert_diagnosis('xray', 1)

    create_pres_test_table()
    insert_diagnosis('cycle', 1)

    create_pres_symptoms_table()
    insert_diagnosis('pregnancy', 1)

    create_payments_table()
    insert_payment(1020, 1)
    
    print(get_history(1))