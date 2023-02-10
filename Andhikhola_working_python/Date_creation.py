# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 21:54:06 2023

@author: admin
"""
import pandas as pd
import matplotlib.pyplot as plt
# Create an empty list to store the dates
dates = []

# Define the months of the year
months = ["Shrawan", "Bhadra", "Ashwin", "Kartik", "Mangsir", "Poush", "Magh", "Falgun", "Chaitra", "Baishakh", "Jestha", "Ashadh"]

# Loop through the years and months
for year in range(1960, 1980):
    for month in months:
        for day in range(1, 32):
            date = month + " " + str(day) + ", " + str(year)
            dates.append(date)

# Convert the list of dates to a DataFrame
dates_df = pd.DataFrame(dates, columns=['Dates'])

# Concatenate the dates DataFrame with the original dataframe
result_df = pd.concat([dates_df, result_df], axis=1)

result_df.to_excel('Date.xlsx', index=False)
