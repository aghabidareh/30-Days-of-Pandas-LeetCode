import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    countries = world[(world['population'] >= 25_000_000) | (world['area'] >= 3_000_000)]
    return countries[['name' , 'population' , 'area']]