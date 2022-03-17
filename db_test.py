from db_creation import *
from db_insertion import *
from db_queries import *


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
    insert_appointment('3/25/2021', '15:33', 1, 2)
    insert_appointment('3/24/2021', '17:33', 2, 2)

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

    print(get_appointments(2))