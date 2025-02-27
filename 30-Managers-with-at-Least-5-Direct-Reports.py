import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    manager_counts = employee.groupby('managerId').size()
    managers_with_five_reports = manager_counts[manager_counts >= 5].index
    result = employee[employee['id'].isin(managers_with_five_reports)][['name']]
    return result