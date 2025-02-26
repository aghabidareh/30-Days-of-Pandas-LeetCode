import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    order_counts = orders["customer_number"].value_counts()
    max_orders = order_counts.max()
    result = order_counts[order_counts == max_orders].index.tolist()
    return pd.DataFrame({"customer_number": result})