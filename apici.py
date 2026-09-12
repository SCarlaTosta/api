import requests as rs
import pandas as pd


response = rs.get("https://jsonplaceholder.typicode.com/users")

print(response.status_code)
print(response.json())


data = response.json()
for user in data:
    print(f"{user["name"]} ----> {user["email"]}")


for user in data:
    print(user["name"], "--->",user["address"]["city"])



df = pd.DataFrame(data)
print(df)
print(df.head())
print(df.columns)
print(df.shape)
print(df["name"])
print(df[["name", "email"]])