from project import patient_dict, generate_patients, print_patients, update_diagnosis, retrieve_diagnosis
from project_class import Patient
import re
import pytest

def generate():
    patient_dict.clear()
    generate_patients(5)

# testing if, when prompted with 5, the function will generate a dict with 5 patients
def test_generate_patients_len():
    generate()
    assert len(patient_dict) == 5

# testing if, when prompted with 5, the function will generate a dict with objects from Patient class
def test_generate_patients_class():
    generate()
    assert all(isinstance(patient, Patient) for patient in patient_dict.values())

# testing if, after generating patients and trying to print them, the function will output the correct no. of prints
def test_print_patients(capsys):
    generate()
    print_patients()
    captured = capsys.readouterr()
    assert len(captured.out.splitlines()) == 20

# testing if, when trying to update patient diagnosis, the function will allow only diagnosis that are in the allowed diagnosis list
def test_update_diagnosis():
    generate()
    sample_id = list(patient_dict.keys())[0]
    update_diagnosis(sample_id, "FEVER")
    assert patient_dict[sample_id].diagnosis == "FEVER"

    with pytest.raises(ValueError):
        update_diagnosis(sample_id, "RANDOMSTUFF")

# testing if, when prompted with a diagnosis, the function will output the correct no. of prints, if the diagnosis is valid
def test_retrieve_diagnosis(capsys):
    generate_patients(5)
    sample_id1 = list(patient_dict.keys())[0]
    sample_id2 = list(patient_dict.keys())[0]
    update_diagnosis(sample_id1, "FEVER")
    update_diagnosis(sample_id2, "FEVER")
    retrieve_diagnosis("FEVER")
    captured = capsys.readouterr()
    print(captured.out)
    lines = captured.out.splitlines()
    assert len(lines) == 2
    match = re.search(r"Total no\. of individuals diagnosed with FEVER: (\d+)", lines[0])
    assert match is not None

    with pytest.raises(ValueError):
        retrieve_diagnosis("RANDOMSTUFF")