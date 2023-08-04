# EasyEHR: A Streamlined Health Records System

#### Description:

This project aims to create a system similar to Electronic Health Records (EHRs), with a focus on managing patient health information. Its inspiration comes from the [MIMIC-III](https://physionet.org/content/mimiciii/1.4/) dataset, a widely-used benchmark dataset for EHRs.

EHRs play a pivotal role in healthcare by gathering critical patient health information such as diagnoses, lab results, medical images, and clinical notes. This multimodal data resource has been significantly enhancing the effectiveness of clinical risk prediction models, which aim to forecast patient outcomes such as diagnoses, readmission, and mortality. Many of these models are based on deep learning, an advanced machine learning technique capable of automatically identifying relevant and complex patterns from data. Given this backdrop, the relevance of EHRs in integrating artificial intelligence with healthcare to optimize patient wellbeing becomes evident.

#### Project details:

This project introduces a streamlined version of an EHR system, enabling users to generate objects derived from a novel 'Patient' class and store them in a patient dictionary. The **'Patient' class**, defined in project_class.py, features as attributes a subject ID, a diagnosis, and both admission and discharge times, formatted as %Y-%m-%d %H:%M:%S, similar to the MIMIC standard. After the patient cohort generation, it is possible to explore the patient instances dictionary in an user-friendly way. Additionally, custom setters are present for the diagnosis (permitted only if it is part of the accepted diagnosis list) and both admission and discharge times (these must adhere to the %Y-%m-%d %H:%M:%S format, or they are framed as invalid).

Here's a closer look into EasyEHR's functionalities, defined in project.py:

- **Patient Dictionary Generation**: The *generate_patients(n)* function generates a dictionary with randomly initialized 'Patient' objects, where 'n' denotes the number of patients to be included in the dictionary. When 'n' is specified, the system creates a patient_dict with the patient's ID as the key, while their diagnosis, admission time, and discharge time serve as the values.

- **Patient Overview**: The *print_patients()* function should be utilized post dictionary generation. It lists out the EHR details for each patient: their ID, diagnosis, and admission and discharge times.

Moreover, the EasyEHR system includes two additional functions: one that updates a patient's diagnosis and another that retrieves patients based on a specific diagnosis:

- **Diagnosis Integration**: Upon input of a patient's ID and a diagnosis, the *update_diagnostic(id, diag)* function integrates a verified diagnosis into the corresponding record, as long as it's included in the list of allowed diagnosis.

- **Diagnosis Lookup**: With a specific diagnosis as input, as long as it's included in the list of allowed diagnosis, the *retrieve_diagnostic(diag)* function outputs the IDs of all patients with that diagnosis and provides the total number of diagnosed individuals.

In addition, the project also provides a requirements.txt file listing the libraries used, and a test_project.py file, with tests to ensure that the proposed functions are working as expected.

In summary, EasyEHR serves as a basic model for electronic health records (EHR) management, inspired by [MIMIC-III](https://physionet.org/content/mimiciii/1.4/). Its potential for expansion is vast: from introducing additional properties found in the authentic MIMIC-III to the 'Patient' class, to incorporating more advanced visualization tools to obtain more profound patient insights. Beyond its analytic capabilities, EasyEHR can also act as a simple EHR dataset generator.

## This is EasyEHR. I hope you enjoy it!
