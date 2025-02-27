import pandas as pd


def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    red_company = company[company['name'] == 'RED']
    if red_company.empty:
        return sales_person[['name']]
    red_com_id = red_company['com_id'].iloc[0]
    sales_with_red = orders[orders['com_id'] == red_com_id]['sales_id'].unique()
    all_salespeople = sales_person['sales_id']
    sales_no_red = all_salespeople[~all_salespeople.isin(sales_with_red)]
    result = sales_person[sales_person['sales_id'].isin(sales_no_red)][['name']]

    return result
