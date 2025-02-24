import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    unique_salaries = employee['salary'].drop_duplicates()
    sorted_salaries = unique_salaries.sort_values(ascending=False)
    if N > len(sorted_salaries) or N <= 0:
        nth_salary = None
    else:
        nth_salary = sorted_salaries.iloc[N - 1]
    
    result = pd.DataFrame({f'getNthHighestSalary({N})': [nth_salary]})

    return result