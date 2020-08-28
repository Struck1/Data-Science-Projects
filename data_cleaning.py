# salary parsing

import pandas as pd

df = pd.read_csv("glassdoor_jobs.csv")

print(type(df["Salary Estimate"][0]))

print(df)