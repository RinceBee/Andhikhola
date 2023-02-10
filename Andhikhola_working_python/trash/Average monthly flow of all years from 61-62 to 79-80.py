# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 11:50:11 2023

@author: kumar
"""
# This code reads the monthly data from a time series ( all the years) from the
# excel file to  calculate monthly average 
import pandas as pd

# Define the range of tabs to be loaded
tabs = ['61-62', '62-63', '63-64', '64-65', '65-66', '66-67', '67-68', '68-69', '69-70', '70-71', '71-72', '72-73', '73-74', '74-75', '75-76', '76-77', '77-78', '78-79', '79-80']

# Create a list to store the average dataframes
average_dfs = []

# Loop through each tab and load the data
for tab in tabs:
    df = pd.read_excel('Andhikhola_foraverage.xlsx', sheet_name=tab, usecols="B:M")
    df = df.iloc[6:, :]
    averages = df.mean(axis=0)
    averages_df = pd.DataFrame(averages).T
    averages_df["Tab"] = tab
    average_dfs.append(averages_df)

# Concatenate all the dataframes into a single dataframe
result_df = pd.concat(average_dfs)

# Define the months of the year
months = ["Shrawan", "Bhadra", "Ashwin", "Kartik", "Mangsir", "Poush", "Magh", "Falgun", "Chaitra", "Baishakh", "Jestha", "Ashadh", "Fiscal year"]

# Insert the months in the first row of the DataFrame
result_df.columns = months

# Save the DataFrame to the same Excel file
result_df.to_excel('Average_monthly_flow_for_all_years_3.xlsx', index=False)



