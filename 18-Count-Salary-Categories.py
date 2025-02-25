import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low_salary = len(accounts[accounts['income'] < 20000])
    average_salary = len(accounts[(accounts['income'] >= 20000) & (accounts['income'] <= 50000)])
    high_salary = len(accounts[accounts['income'] > 50000])
    new_data = pd.DataFrame({
        'category' : ['Low Salary', 'Average Salary', 'High Salary'],
        'accounts_count' : [low_salary, average_salary, high_salary]
    })
    return new_data