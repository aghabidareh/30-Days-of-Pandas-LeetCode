import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee.drop_duplicates(inplace=True , subset='salary')
    if len(employee) >= 2:
        second = employee.sort_values(by='salary' , ascending=False).iloc[1,1]
    else:
        second = None
    return pd.DataFrame({'SecondHighestSalary' : [second]})