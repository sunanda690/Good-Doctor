#!/usr/bin/python

import psycopg2
from config import config
from datetime import datetime, date


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


def get_patient_name(patient_id):
    name = ""
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        sql = "SELECT name FROM patient where patient_id=%s;"
        cur.execute(sql, (patient_id, ))
        
        name = cur.fetchone()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return name


def get_patient_id(username):
    id = -1
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        sql = "SELECT patient_id FROM patient where username=%s;"
        cur.execute(sql, (username, ))
        
        id = cur.fetchone()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return id


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


def get_doctor_name(doctor_id):
    name = ""
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        sql = "SELECT name FROM doctor where doctor_id=%s;"
        cur.execute(sql, (doctor_id, ))
        
        name = cur.fetchone()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return name


def get_doctor_id(username):
    id = -1
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        sql = "SELECT doctor_id FROM doctor where username=%s;"
        cur.execute(sql, (username, ))
        
        id = cur.fetchone()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return id


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


def get_spec_id(speciality):
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


def get_slot_id(slot):
    slot_id = -1
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        sql = "SELECT slot_id FROM slots where start_time=%s and end_time=%s;"
        cur.execute(sql, (slot[0],slot[1]))
        slot_id = cur.fetchone()[0]      
        
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return slot_id


def get_qual_id(qual_name):
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


def get_symptom_id(symptom):
    symp_id = -1
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        sql = "SELECT symptom_id FROM symptom where name=%s;"
        cur.execute(sql, (symptom,))
        symp_id = cur.fetchone()[0]      
        
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return symp_id


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


def get_best_doctor(symptoms_list, pref_time):
    conn = None
    best_doc_id = -1
    pref_time = datetime.strptime(pref_time, '%H:%M').time()
    pref_time = datetime.combine(date.today(), pref_time)

    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        priority = dict()
        priority['chest pain'] = 100
        priority['breathing trouble'] = 90
        priority['burns'] = 80
        priority['fracture'] = 70
        priority['urinary problems'] = 60
        priority['diabetes'] = 50
        priority['skin rashes'] = 40
        priority['head ache'] = 30
        priority['stomach ache'] = 20
        priority['throat infection'] = 19
        priority['nose infection'] = 17
        priority['ear infection'] = 15
        priority['cold'] = 10

        spec = dict()
        spec['chest pain'] = 'cardiology'
        spec['breathing trouble'] = 'pulmonology'
        spec['burns'] = 'surgury'
        spec['fracture'] = 'orthopedia'
        spec['urinary problems'] = 'urology'
        spec['diabetes'] = 'endocrinology'
        spec['skin rashes'] = 'dermetalogy'
        spec['head ache'] = 'neurology'
        spec['stomach ache'] = 'gastroenterology'
        spec['throat infection'] = 'ENT'
        spec['nose infection'] = 'ENT'
        spec['ear infection'] = 'ENT'
        spec['cold'] = 'physician'

        major_problem = 'cold'

        for s in symptoms_list:
            if priority[s] > priority[major_problem]:
                major_problem = s

        speciality = spec[major_problem]
        # print(speciality)
        spec_id = get_spec_id(speciality)
        doc_ids = []

        sql = """
        SELECT doctor_id FROM specialized  
        where spec_id=%s;
        """

        cur.execute(sql, (spec_id, ))

        for i in range(cur.rowcount):
            doc_ids.append(cur.fetchone())
               
        min_slots = []

        for docid in doc_ids:
            docid = docid[0]

            sql = """
            SELECT s.start_time, s.end_time FROM has_slots hs
            left join slots s on hs.slot_id=s.slot_id 
            where hs.doctor_id=%s;
            """

            cur.execute(sql, (docid, ))

            slots = []
            for i in range(cur.rowcount):
                slot = cur.fetchone()    
                start = datetime.combine(date.today(), slot[0])
                end = datetime.combine(date.today(), slot[1])
                
                # print((end - pref_time).days)
                # print((start - pref_time).days)
                if (start-pref_time).days<0 and (end - pref_time).days>=0:
                    cur.close()
                    conn.close()
                    # print("here")
                    return (docid, slot)

                elif (start-pref_time).days>=0 and (end - pref_time).days>=0:
                    slots.append(slot)

            # print(slots)

            start = datetime.combine(date.today(), slots[0][0])
            end = datetime.combine(date.today(), slots[0][1])

            delta = (start - pref_time).seconds
            best_slot = slots[0]

            for s in slots:
                start = datetime.combine(date.today(), s[0])
                end = datetime.combine(date.today(), s[1])
                
                if (start - pref_time).seconds<delta:
                    best_slot = s
                    delta = (start - pref_time).seconds

            # print(docid)
            min_slots.append((docid,best_slot))

        start = datetime.combine(date.today(), min_slots[0][1][0])
        end = datetime.combine(date.today(), min_slots[0][1][1])
        # pref_time = datetime.combine(date.today(), pref_time)

        delta = (start - pref_time).seconds
        best_slot = min_slots[0][1]
        best_doc_id = min_slots[0][0]
        # print(min_slots)

        for s in min_slots:
            start = datetime.combine(date.today(), s[1][0])
            end = datetime.combine(date.today(), s[1][1])
            
            if (start - pref_time).seconds<delta:
                best_slot = s[1]
                best_doc_id = s[0]
                delta = (start - pref_time).seconds
              

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return (best_doc_id, best_slot)
