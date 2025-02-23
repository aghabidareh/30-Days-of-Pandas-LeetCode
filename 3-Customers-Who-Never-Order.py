import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    result = customers[~customers['id'].isin(orders['customerId'])]
    result.rename({'name' : 'Customers'} , inplace=True , axis=1)
    return pd.DataFrame(result['Customers'])