from db_creation import *
from db_insertion import *
from db_queries import *


if __name__ == '__main__':
    create_patient_table()
    insert_patient("abhi", "Abhilash Datta", "abhi.com", "abcd", "760", "21")
    insert_patient("rrohit", "Rohit Raj", "rrohit.com", "wxyz", "727", "21")
    print(search_patient("rrohit", "wxyz"))

    create_doctor_table()
    insert_doctor("A", "Dr. A", "a.com", "a", "7602045111", "21", "3")
    insert_doctor("B", "Dr. B", "b.com", "b", "7602045111", "21", "3")
    insert_doctor("C", "Dr. C", "c.com", "c", "7602045111", "21", "3")
    print(search_doctor("A", "a"))

    create_specialization_table()
    insert_specialization("cardio")
    insert_specialization("gastroenterology")
    insert_specialization("ENT")
    insert_specialization("Eye")
    print(get_spec_id("ENT"))

    create_specialized_table()
    insert_specialized(2,1)
    insert_specialized(2,2)
    insert_specialized(2,3)

    create_qualification_table()
    insert_qualification('MBBS')
    insert_qualification('MS')
    print(get_qual_id('MS'))

    create_qualified_table()
    insert_qualified(1,1,2020,'iitkgp')
    insert_qualified(2,1,2021,'MIT')

    create_slots_table()
    insert_slot('03:00', '16:30')
    insert_slot('04:00', '17:30')
    insert_slot('05:00', '18:30')
    insert_slot('06:00', '19:30')
    insert_slot('07:00', '20:30')
    insert_slot('08:00', '21:30')

    insert_slot('12:00', '19:30')
    insert_slot('13:00', '20:30')
    insert_slot('14:00', '21:30')

    create_has_slots_table()
    insert_has_slot(get_slot_id(('12:00', '19:30')),get_doctor_id('A'))
    insert_has_slot(get_slot_id(('13:00', '20:30')),get_doctor_id('B'))
    insert_has_slot(get_slot_id(('14:00', '21:30')),get_doctor_id('C'))

    create_prescription_table()
    insert_prescription(get_patient_id('abhi'),get_doctor_id('A'))

    create_symptom_table()
    insert_symptom('cough')
    insert_symptom('cold')
    insert_symptom('congestion')
    insert_symptom('stomach ache')
    insert_symptom('head ache')
    insert_symptom('burns')

    create_has_symptom_table()
    insert_has_symptom(1,get_symptom_id('stomach ache'))
    insert_has_symptom(1,get_symptom_id('cold'))
    insert_has_symptom(1,get_symptom_id('cough'))

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

    print(get_best_doctor(['stomach ache', 'cold'], '11:30'))
    print(get_all_symptoms())

    print(get_patient_details('abhi'))
    print(get_doctor_details('A'))

    print(get_doctor_qualifications('A'))

    print(get_all_specs())

    print((get_all_slots()))

    print(get_doctor_slots(1))