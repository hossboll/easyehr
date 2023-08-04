from project_class import Patient
from datetime import datetime, timedelta
import random

# setting number of patients for patient generation
no_patients = 5
# initializing empty patient dictionary
patient_dict = {}

""" Generating and printing a randomized patient cohort
"""
def main():
    generate_patients(no_patients)
    print_patients()

""" generate_patients(n)
    Generates random patients, which are objects from the 'Patient' class, and stores them in a patient's dictionary (patients_dict)
    n: int, number of patients to be generated
"""
def generate_patients(n):
    for _ in range(n):
        # creating the admittime and the dischtime randomly
        days_ago = random.randint(1, 365) # generating a random day
        seconds_ago = random.randint(1, 86400) # generating random seconds

        random_admittime_dt = datetime.now() - timedelta(days=days_ago, seconds=seconds_ago) # subtracting the difference obtained with random days/secs from today's date
        stay_duration_days = random.randint(1, 30) # deciding length of stay, considering maximum = 30 days
        stay_duration_seconds = random.randint(1, 86400)

        random_dischtime_dt = random_admittime_dt + timedelta(days=stay_duration_days, seconds=stay_duration_seconds) # creating discharge time based on length of stay
        random_admittime = random_admittime_dt.strftime('%Y-%m-%d %H:%M:%S') # admission time
        random_dischtime = random_dischtime_dt.strftime('%Y-%m-%d %H:%M:%S') # discharge time
        random_diagnosis = random.choice(Patient.diagnosis_list) # choosing randomly a diagnosis between the allowed diagnosis

        patient = Patient(admittime=random_admittime, dischtime=random_dischtime, diagnosis=random_diagnosis) # instantiating a patient
        patient_dict[patient.subject_id] = patient # including them in the patient dictionary


""" print_patients()
    After generating the dictionary of random patients, prints information contained in their EHRs
"""
def print_patients():
    # for each unique id present in the dictionary, print their data in an user-friendly way
    for id, patient in patient_dict.items():
        print(f"ID: {id}")
        print(f"Admission Time: {patient.admittime}")
        print(f"Discharge Time: {patient.dischtime}")
        print(f"Diagnosis: {patient.diagnosis}")

""" update_diagnosis(id, diag)
    Given a patient's ID and a diagnosis, updates their diagnosis accordingly
    id: int, represents a unique patient's ID
    diag: str, represents the diagnosis to be assigned
"""
def update_diagnosis(id, diag):
    if diag in Patient.diagnosis_list: # if the diagnosis is allowed, proceed
        try:
            patient = patient_dict[id] # retrieving patient
            patient.diagnosis = diag # assigning diagnosis
        except KeyError:
            print("This ID doesn't exist.")
    else:
        raise ValueError("Diagnosis is invalid.")

""" retrieve_diagnosis(diag)
    Given a diagnosis, returns the total number of individuals with that diagnosis, and a list of their unique ID's
    diag: str, represents the diagnosis to be assigned
"""
def retrieve_diagnosis(diag):
    if diag not in Patient.diagnosis_list:
        raise ValueError("Diagnosis is invalid.")

    tot_diag = 0
    list_diag_ids = []
    for id, p in patient_dict.items():
        if p.diagnosis == diag: # if the patient's diagnosis matches with the query
            tot_diag += 1 # add 1 to total count of patients with that diagnosis
            list_diag_ids.append(p.subject_id) # save patient's id to the list

    print(f"Total no. of individuals diagnosed with {diag}: {tot_diag}")
    print(list_diag_ids)

if __name__ == "__main__":
    main()