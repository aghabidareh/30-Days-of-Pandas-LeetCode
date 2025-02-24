import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    if employee.empty or department.empty:
        return pd.DataFrame(columns=['Department','Employee', 'Salary'])

    merged = employee.merge(department , left_on='departmentId' , right_on='id' , suffixes=('_employee' , '_department'))
    highest_salaries = merged.groupby('departmentId').apply(lambda x: x[x['salary'] == x['salary'].max()])
    highest_salaries = highest_salaries.reset_index(drop=True)
    result = highest_salaries[['name_department', 'name_employee', 'salary']]
    result.columns = ['Department','Employee', 'Salary']
    return result