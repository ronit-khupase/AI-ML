#14. Write a Python program to implement Data Normalization / Standardization. 

import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

df = pd.read_csv("preprocessing.csv")

# Select numeric data
num = df.select_dtypes(include=['number'])

# Normalization
scaler = MinMaxScaler()
norm = scaler.fit_transform(num)

print("Normalized Data:\n", norm)

# Standardization (optional)
# scaler = StandardScaler()
# std = scaler.fit_transform(num)


df['Salary']=scaler.fit_transform(df[['Salary']]) #single Column
print("Salary normalized\n",df['Salary'])