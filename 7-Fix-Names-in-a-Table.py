import pandas as pd


def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    def func(x):
        return x.capitalize()

    users['name'] = users['name'].apply(func)
    return users.sort_values(by='user_id')