import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees["time_spent"] = employees["out_time"] - employees["in_time"]
    employees = employees.groupby(["event_day", "emp_id"], as_index=False)["time_spent"].sum()
    employees.rename(columns={"event_day": "day", "time_spent": "total_time"}, inplace=True)
    return employees