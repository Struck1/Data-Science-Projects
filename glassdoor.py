import glassdoor_scraping as gs
import pandas as pd
path = r"C:\Users\ASUS\Desktop\Machine Learning\chromedriver"

#df = gs.get_jobs('data scientist', 1000, False, path=path)

#df.to_csv("glassdoor_data.csv", index = False)

df = pd.read_csv("glassdoor_jobs.csv")
print(df.head())
