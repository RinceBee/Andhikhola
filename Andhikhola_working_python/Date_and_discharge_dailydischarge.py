# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 21:56:55 2023

@author: admin
"""
import pandas as pd
import matplotlib.pyplot as plt

# Create a list of tabs to read
tabs = ["61-62", "62-63", "63-64", "64-65", "65-66", "66-67", "67-68", "68-69", "69-70", "70-71", "71-72", "72-73", "73-74", "74-75", "75-76", "76-77", "77-78", "78-79", "79-80"]

# Create an empty list to store the data
data_list = []

# Iterate through the tabs
for tab in tabs:
    # Load the excel file
    df = pd.read_excel('Andhikhola_Allarray_1.xlsx', sheet_name=tab)
    # Select the data in the range B7:M38
    data = df.iloc[5:38, 1:13]
    # Concatenate all columns into a single column
    data = pd.concat([data[col] for col in data.columns], axis=0)
    # Append the data to the list
    data_list.append(data)

# Concatenate all the data into a single dataframe
data = pd.concat(data_list)

# Reset the index
data = data.reset_index(drop=True)

# Create an empty list to store the dates
dates = []

# Define the months of the year
months = ["Shrawan", "Bhadra", "Ashwin", "Kartik", "Mangsir", "Poush", "Magh", "Falgun", "Chaitra", "Baishakh", "Jestha", "Ashadh"]

# Loop through the years and months
for year in range(2061, 2080):
    for month in months:
        for day in range(1, 33):
            if month == "Baishakh" and day == 1:
                year += 1
            date = month + " " + str(day) + ", " + str(year)
            dates.append(date)

# Convert the list of dates to a DataFrame
dates_df = pd.DataFrame(dates, columns=['Dates'])
# Concatenate the dates DataFrame with the original dataframe
result_df = pd.concat([dates_df, data], axis=1)
#result_df.to_excel('Daily_discharge.xlsx', index=False)
data.plot(kind='line')
plt.show()


