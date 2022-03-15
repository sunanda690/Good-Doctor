#!/usr/bin/python

import psycopg2
from config import config


def create_patient_table():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        drop table if exists patient;
        """,
        """
        CREATE TABLE patient (
            patient_id SERIAL PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL
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


def insert_signup_info(username, email, password):
    """ insert a new vendor into the vendors table """
    sql = """INSERT INTO patient(username, email, password)
             VALUES(%s, %s, %s) RETURNING patient_id, username, email, password;"""
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
        cur.execute(sql, (username, email, password))
        # get the generated id back
        patient_details = cur.fetchone()
        print(patient_details,"inserted")
        # commit the changes to the database
        conn.commit()
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

# if __name__ == '__main__':
#     create_patient_table()
#     insert_signup_info("abh", "abh.com", "ajsb")
#     insert_signup_info("acbh", "acbh.com", "acjsb")
#     print(search_patient("abh", "ajsb"))



