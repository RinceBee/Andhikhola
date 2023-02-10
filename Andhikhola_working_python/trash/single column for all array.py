# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 10:07:22 2023

@author: kumar
"""

import pandas as pd

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

# Save the data to a new Excel file
data.to_excel('new_file_3.xlsx', index=False)
