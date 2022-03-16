#!/usr/bin/python

import psycopg2
from config import config

# Patient

def create_patient_table():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        drop table if exists patient cascade;
        """,
        """
        CREATE TABLE patient (
            patient_id SERIAL PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            name VARCHAR(255) NOT NULL, 
            email VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL,
            mobile_number VARCHAR(255) NOT NULL,
            age int NOT NULL
        )
        """,
        )
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


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

# Doctor

def create_doctor_table():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        drop table if exists doctor cascade;
        """,
        """
        CREATE TABLE doctor (
            doctor_id SERIAL PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            name VARCHAR(255) NOT NULL, 
            email VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL,
            mobile_number VARCHAR(255) NOT NULL,
            age int NOT NULL,
            experience int NOT NULL
        )
        """,
        )
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


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


# Specialization

def create_specialization_table():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        drop table if exists specialization cascade;
        """,
        """
        CREATE TABLE specialization (
            spec_id SERIAL PRIMARY KEY,
            speciality VARCHAR(255) NOT NULL
        )
        """,
        )
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


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

# specialized    

def create_specialized_table():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        drop table if exists specialized cascade;
        """,
        """
        CREATE TABLE specialized (
            spec_id INTEGER,
            doctor_id INTEGER, 
            PRIMARY KEY(spec_id, doctor_id),
            FOREIGN KEY(spec_id) REFERENCES specialization,
            FOREIGN KEY(doctor_id) REFERENCES doctor
        )
        """,
        )
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()    


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


# Qualification

def create_qualification_table():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        drop table if exists qualification cascade;
        """,
        """
        CREATE TABLE qualification (
            qual_id SERIAL PRIMARY KEY,
            qual_name VARCHAR(255) NOT NULL
        )
        """,
        )
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


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

# Qualified

def create_qualified_table():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        drop table if exists qualified cascade;
        """,
        """
        CREATE TABLE qualified (
            qual_id INTEGER,
            doctor_id INTEGER, 
            procurement_year INTEGER,
            institute VARCHAR(255) NOT NULL,
            PRIMARY KEY(qual_id, doctor_id),
            FOREIGN KEY(qual_id) references qualification,
            FOREIGN KEY(doctor_id) references doctor
        )
        """,
        )
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


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

# Slots

def create_slots_table():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        drop table if exists slots cascade;
        """,
        """
        CREATE TABLE slots (
            slot_id SERIAL PRIMARY KEY,
            start_time time NOT NULL,
            end_time time NOT NULL
        )
        """,
        )
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


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

# has slots

def create_has_slots_table():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        drop table if exists has_slots cascade;
        """,
        """
        CREATE TABLE has_slots (
            slot_id INTEGER NOT NULL,
            doctor_id INTEGER NOT NULL,
            PRIMARY KEY(slot_id, doctor_id),
            FOREIGN KEY(slot_id) references slots,
            FOREIGN KEY(doctor_id) references doctor
        )
        """,
        )
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


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

# Prescription

def create_prescription_table():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        drop table if exists prescription cascade;
        """,
        """
        CREATE TABLE prescription (
            pres_id SERIAL PRIMARY KEY,
            patient_id INTEGER NOT NULL,
            doctor_id INTEGER NOT NULL,
            FOREIGN KEY(patient_id) references patient,
            FOREIGN KEY(doctor_id) references doctor
        )
        """,
        )
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


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


# Symptoms

def create_symptom_table():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        drop table if exists symptom cascade;
        """,
        """
        CREATE TABLE symptom (
            symptom_id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        )
        """,
        )
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


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


# has symptom

def create_has_symptom_table():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        drop table if exists has_symptom cascade;
        """,
        """
        CREATE TABLE has_symptom (
            patient_id INTEGER NOT NULL,
            symptom_id INTEGER NOT NULL,
            PRIMARY KEY(patient_id, symptom_id),
            FOREIGN KEY(patient_id) references patient,
            FOREIGN KEY(symptom_id) references symptom
        )
        """,
        )
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


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

# appointments

def create_appointments_table():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        drop table if exists appointments cascade;
        """,
        """
        CREATE TABLE appointments (
            appointment_id SERIAL PRIMARY KEY,
            appointment_date DATE NOT NULL,
            appointment_time TIME NOT NULL,
            patient_id INTEGER NOT NULL,
            doctor_id INTEGER NOT NULL,
            FOREIGN KEY(patient_id) references patient,
            FOREIGN KEY(doctor_id) references doctor
        )
        """,
        )
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


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

# history

def create_history_table():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        drop table if exists history cascade;
        """,
        """
        CREATE TABLE history (
            history_id SERIAL PRIMARY KEY,
            appointment_id INTEGER NOT NULL,
            patient_id INTEGER NOT NULL,
            FOREIGN KEY(patient_id) references patient,
            FOREIGN KEY(appointment_id) references appointments
        )
        """,
        )
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


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

# pres_medicines

def create_pres_medicines_table():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        drop table if exists pres_medicines cascade;
        """,
        """
        CREATE TABLE pres_medicines (
            medicine VARCHAR(255) NOT NULL,
            pres_id INTEGER NOT NULL,
            PRIMARY KEY(medicine, pres_id),
            FOREIGN KEY(pres_id) references prescription
        )
        """,
        )
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


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

# pres_diagnosis

def create_pres_diagnosis_table():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        drop table if exists pres_diagnosis cascade;
        """,
        """
        CREATE TABLE pres_diagnosis (
            diagnosis VARCHAR(255) NOT NULL,
            pres_id INTEGER NOT NULL,
            PRIMARY KEY(diagnosis, pres_id),
            FOREIGN KEY(pres_id) references prescription
        )
        """,
        )
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


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

# pres_test

def create_pres_test_table():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        drop table if exists pres_test cascade;
        """,
        """
        CREATE TABLE pres_test (
            test VARCHAR(255) NOT NULL,
            pres_id INTEGER NOT NULL,
            PRIMARY KEY(test, pres_id),
            FOREIGN KEY(pres_id) references prescription
        )
        """,
        )
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


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

# pres_symptoms

def create_pres_symptoms_table():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        drop table if exists pres_symptoms cascade;
        """,
        """
        CREATE TABLE pres_symptoms (
            symptoms VARCHAR(255) NOT NULL,
            pres_id INTEGER NOT NULL,
            PRIMARY KEY(symptoms, pres_id),
            FOREIGN KEY(pres_id) references prescription
        )
        """,
        )
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


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


# payments

def create_payments_table():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        drop table if exists payments cascade;
        """,
        """
        CREATE TABLE payments (
            payment_id SERIAL PRIMARY KEY,
            amount INTEGER NOT NULL,
            appointment_id INTEGER NOT NULL,
            FOREIGN KEY(appointment_id) references appointments
        )
        """,
        )
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


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
    insert_history(1,2)

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
    