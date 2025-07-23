import pandas as pd
import sqlite3

df_ad_sales = pd.read_csv(r"D:\Skanath Kumar Files\Ecommerce_AI_Project\Ad_Sales.csv")
df_eligibility = pd.read_csv(r"D:\Skanath Kumar Files\Ecommerce_AI_Project\Eligibility_Table.csv")
df_total_sales = pd.read_csv(r"D:\Skanath Kumar Files\Ecommerce_AI_Project\Total_Sales.csv")

conn_sql = sqlite3.connect("ecommerce.db")

df_ad_sales.to_sql("ad_sales", conn_sql, if_exists="replace", index=False)
df_eligibility.to_sql("eligibility", conn_sql, if_exists="replace", index=False)
df_total_sales.to_sql("total_sales", conn_sql, if_exists="replace", index=False)

conn_sql.commit()
conn_sql.close()

print("Data Loaded successfully")