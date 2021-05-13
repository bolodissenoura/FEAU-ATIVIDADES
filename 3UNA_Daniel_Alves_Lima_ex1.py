import pandas as pd
from datetime import date

df = pd.read_table("2016I01Fa.SJC")

df["hpF2-h’F"] = df["hpF2"] - df["h'F"]
print("Redutor: AUTOMATICO PELO POLINOMIO")
today = date.today()
print("Data:", today)
print(df)
input()