#!/usr/bin/python

import psycopg2
from config import config

def create_patient_table():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        drop table if exists patient cascade;
        """,
        """
        CREATE TABLE patient (
            patient_id SERIAL PRIMARY KEY,
            username VARCHAR(255) NOT NULL UNIQUE,
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










