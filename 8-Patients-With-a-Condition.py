import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    rsult = patients[patients['conditions'].str.contains(r'(^| )DIAB1')]
    return rsult[['patient_id', 'patient_name', 'conditions']]