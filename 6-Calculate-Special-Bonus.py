import pandas as pd


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    def func(row):
        if row['employee_id'] % 2 != 0 and not row['name'].startswith('M'):
            return row['salary']
        else:
            return 0

    employees['bonus'] = employees.apply(func, axis=1)
    employees.sort_values(by='employee_id', inplace=True)
    return employees[['employee_id', 'bonus']]