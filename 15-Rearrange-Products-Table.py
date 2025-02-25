import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    products = products.melt(id_vars=["product_id"], var_name="store", value_name="price")
    products.dropna(subset=["price"], inplace=True)
    products.reset_index(drop=True, inplace=True)
    return products