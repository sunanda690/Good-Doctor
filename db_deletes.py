#!/usr/bin/python

import psycopg2
from config import config

def delete_appointment(app_id):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        sql = """
            ALTER TABLE appointments ADD FOREIGN KEY (appointment_id)
            REFERENCES history(appointment_id) ON DELETE CASCADE;
        """
        cur.execute(sql)

        sql = "DELETE FROM appointments WHERE appointment_id=%s;"
        cur.execute(sql, (app_id,))
        
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
