import requests  
response = requests.get('https://api.exchangerate.host/latest')
import json
data = json.loads(response.text) 
import pandas as pd
df = pd.DataFrame(data)  
new_dict = {}  
x=2 
y=1

column_name = input("please enter a column you would like to see for the exchange convert rate")  
print(df) 

#column_name = 'rates'  # Replace with the actual column name 
if column_name in df.columns:  
    selected_column = df[column_name]
    print(selected_column)
else:
    print(f"Column '{column_name}' not found in the DataFrame.")  
#for loop checking for if rates are similar to the last reconginzed one
for i in range(0, 1000):  # Integer range (0 to 999)
    float_i = i / 10.0  # Convert to float (0.0 to 99.9), a special way since can't just iterate by 0.1
    for j in range(0, 100):
        if (float_i == df[column_name]).any():
            new_dict["key" + str(j)] = float_i 
      
new_currency = df[column_name]  
while x>y: #Having a dictonary to store the last stock price. It compares and sees (with the perivous calculation) if there is a difference in price and always update the dictinary.  
    new_dict[x] = new_dict[y] 
    x = x-1  
print(df["base"])
print(new_dict)