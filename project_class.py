from datetime import datetime

# Patient class is inspired by the EHR format, more specifically on how patient information is stored in the MIMIC-III dataset:
# more about MIMIC-III here: https://physionet.org/content/mimiciii-demo/1.4/
class Patient:
    tot_id = 0
    diagnosis_list = ["SEPSIS", "HEPATITIS B", "HUMERAL FRACTURE", "ALCOHOLIC HEPATITIS",
                          "STROKE/TIA", "UNSTABLE ANGINA", "RESPIRATORY DISTRESS", "FEVER"] # list of allowed diagnosis

    def __init__(self, admittime=None, dischtime=None, diagnosis=None):
        self.subject_id = Patient.tot_id
        Patient.tot_id += 1 # assigning patient's unique id

        if admittime is None:
            self._admittime = datetime.now().strftime('%Y-%m-%d %H:%M:%S') # setting admission time to "now" if that isn't explicitely mentioned
        else:
            self._admittime = admittime

        self._dischtime = dischtime
        self._diagnosis = diagnosis


    @property # getter for admittime, returning time of patient admission
    def admittime(self):
        return self._admittime

    @admittime.setter # setter for admittime, assuring that time will be in the '%Y-%m-%d %H:%M:%S' format
    def admittime(self, time):
        try:
            datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
            self._admittime = time
        except ValueError:
            raise ValueError("Time is not formatted correctly.")


    @property
    def dischtime(self): # getter for admittime, returning time of patient discharge
        return self._dischtime

    @dischtime.setter
    def dischtime(self, time): # setter for dischtime, assuring that time will be in the '%Y-%m-%d %H:%M:%S' format
        try:
            datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
            self._dischtime = time
        except ValueError:
            raise ValueError("Time is not formatted correctly.")


    @property
    def diagnosis(self): # setter for diagnosis, returning patient diagnosis
        return self._diagnosis

    @diagnosis.setter # setter for diagnosis, assuring that the input diagnosis is in the list of allowed diagnosis
    def diagnosis(self, a_diagnosis):
        if a_diagnosis in Patient.diagnosis_list:
            self._diagnosis = a_diagnosis
        else:
            raise ValueError("Invalid diagnosis.")
