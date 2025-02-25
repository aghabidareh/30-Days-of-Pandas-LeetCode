import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    data = pd.DataFrame(scores)
    data['rank'] = data["score"].rank(method="dense", ascending=False).astype(int)
    result = data[["score", "rank"]].sort_values(by=["score"], ascending=False)
    return result