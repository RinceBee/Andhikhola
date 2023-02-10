# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 17:10:15 2023

@author: kumar
"""

# This code reads the monthly data from a time series ( all the years) from the
# excel file to  calculate monthly average 
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

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

# Define the months of the year
#months = ["Chaitra", "Baishakh", "Jestha", "Ashadh", "Shrawan", "Bhadra", "Ashwin", "Kartik", "Mangsir", "Poush", "Magh", "Falgun"]

# Create a new Excel writer object
writer = pd.ExcelWriter("Monthly_Data.xlsx", engine='xlsxwriter')

# Loop through each month
for i, month in enumerate(months):
    # Select the data for the current month
    month_data = result_df[month]
    
    # Convert the data to a DataFrame
    month_data = pd.DataFrame(month_data)
    
    # Add the "Fiscal year" column to the DataFrame
    month_data["Fiscal year"] = result_df["Fiscal year"]
    
    # Write the data to a new sheet in the Excel file
    month_data.to_excel(writer, sheet_name=month, startcol=0, startrow=0, index=False)
    
# Save the Excel file
writer.save()


#result_df = result_df[["Chaitra", "Baishakh", "Jestha", "Ashadh", "Shrawan", "Bhadra", "Ashwin", "Kartik", "Mangsir", "Poush", "Magh", "Falgun", "Fiscal year"]]
#averages = result_df.mean(axis=0)
#averages.plot(kind='line', marker="D", label = 'averages')
#plt.xlabel("Months")
#plt.ylabel("Discharge(m3/s)")
#plt.title("Mean Monthly Discharge over all years")
#plt.savefig("hydrograph.png")
#plt.show()