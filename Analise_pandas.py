import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8")

df = pd.read_excel("compras.xlsx")

print(df.head())

df["Data Pedido"] =  pd.to_datetime(df["Data Pedido"])

df.dtypes