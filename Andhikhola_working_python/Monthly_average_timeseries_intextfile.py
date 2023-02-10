# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 11:17:22 2023

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

#averages = result_df.mean(axis=0)
#result_df.loc["Average"] = averages
#result_df.to_excel('Average_monthly_flow_for_all_years_5.xlsx', index=True)

result_df = result_df[["Chaitra", "Baishakh", "Jestha", "Ashadh", "Shrawan", "Bhadra", "Ashwin", "Kartik", "Mangsir", "Poush", "Magh", "Falgun", "Fiscal year"]]
averages = result_df.mean(axis=0)
averages.plot(kind='line', marker="D", label = 'averages')
plt.xlabel("Months")
plt.ylabel("Discharge(m3/s)")
plt.title("Mean Monthly Discharge over all years")
#plt.savefig("hydrograph.png")
#plt.show()

#TO SAVE TEXT FILES
    
years = range(2061, 2080)
result_years_df = pd.DataFrame(columns=["#years"])
for year in years:
    # assuming you have data of baishakh for each year in a variable named `baishakh_data`
    result_years_df = result_years_df.append({"#years": year}, ignore_index=True)

# For Chaitra
result_chaitra_df = result_df[["Chaitra"]]

#append these two columns result_df and  result_years_df
result_chaitra_df.reset_index(drop=True, inplace=True)
result_years_df.reset_index(drop=True, inplace=True)
result_chaitra = pd.concat([result_years_df, result_chaitra_df], axis=1)
result_chaitra = result_chaitra.iloc[:,[-2,-1]]

# Add "#" symbol in front of missing values in 'years' column
result_chaitra["#years"] = result_chaitra.apply(lambda x: "#"+str(x["#years"]) if pd.isna(x["Chaitra"]) else x["#years"], axis=1)

#export to text file
result_chaitra.to_csv('Chaitra_average.txt', sep=' ', index=False)

# For Baishakh
result_Baishakh_df = result_df[["Baishakh"]]

#append these two columns result_df and  result_years_df
result_Baishakh_df.reset_index(drop=True, inplace=True)
result_years_df.reset_index(drop=True, inplace=True)
result_Baishakh = pd.concat([result_years_df, result_Baishakh_df], axis=1)
result_Baishakh = result_Baishakh.iloc[:,[-2,-1]]

# Add "#" symbol in front of missing values in 'years' column
result_Baishakh["#years"] = result_Baishakh.apply(lambda x: "#"+str(x["#years"]) if pd.isna(x["Baishakh"]) else x["#years"], axis=1)

#export to text file
result_Baishakh.to_csv('Baishakh_average.txt', sep=' ', index=False)

# For Jestha
result_Jestha_df = result_df[["Jestha"]]

#append these two columns result_df and  result_years_df
result_Jestha_df.reset_index(drop=True, inplace=True)
result_years_df.reset_index(drop=True, inplace=True)
result_Jestha = pd.concat([result_years_df, result_Jestha_df], axis=1)
result_Jestha = result_Jestha.iloc[:,[-2,-1]]

# Add "#" symbol in front of missing values in 'years' column
result_Jestha["#years"] = result_Jestha.apply(lambda x: "#"+str(x["#years"]) if pd.isna(x["Jestha"]) else x["#years"], axis=1)

#export to text file
result_Jestha.to_csv('Jestha_average.txt', sep=' ', index=False)

# For Ashadh
result_Ashadh_df = result_df[["Ashadh"]]

#append these two columns result_df and  result_years_df
result_Ashadh_df.reset_index(drop=True, inplace=True)
result_years_df.reset_index(drop=True, inplace=True)
result_Ashadh = pd.concat([result_years_df, result_Ashadh_df], axis=1)
result_Ashadh = result_Ashadh.iloc[:,[-2,-1]]

# Add "#" symbol in front of missing values in 'years' column
result_Ashadh["#years"] = result_Ashadh.apply(lambda x: "#"+str(x["#years"]) if pd.isna(x["Ashadh"]) else x["#years"], axis=1)

#export to text file
result_Ashadh.to_csv('Ashadh_average.txt', sep=' ', index=False)

# For Shrawan
result_Shrawan_df = result_df[["Shrawan"]]

#append these two columns result_df and  result_years_df
result_Shrawan_df.reset_index(drop=True, inplace=True)
result_years_df.reset_index(drop=True, inplace=True)
result_Shrawan = pd.concat([result_years_df, result_Shrawan_df], axis=1)
result_Shrawan = result_Shrawan.iloc[:,[-2,-1]]

# Add "#" symbol in front of missing values in 'years' column
result_Shrawan["#years"] = result_Shrawan.apply(lambda x: "#"+str(x["#years"]) if pd.isna(x["Shrawan"]) else x["#years"], axis=1)

#export to text file
result_Shrawan.to_csv('Shrawan_average.txt', sep=' ', index=False)

# For Bhadra
result_Bhadra_df = result_df[["Bhadra"]]

#append these two columns result_df and  result_years_df
result_Bhadra_df.reset_index(drop=True, inplace=True)
result_years_df.reset_index(drop=True, inplace=True)
result_Bhadra = pd.concat([result_years_df, result_Bhadra_df], axis=1)
result_Bhadra = result_Bhadra.iloc[:,[-2,-1]]

# Add "#" symbol in front of missing values in 'years' column
result_Bhadra["#years"] = result_Bhadra.apply(lambda x: "#"+str(x["#years"]) if pd.isna(x["Bhadra"]) else x["#years"], axis=1)

#export to text file
result_Bhadra.to_csv('Bhadra_average.txt', sep=' ', index=False)

# For Ashwin
result_Ashwin_df = result_df[["Ashwin"]]

#append these two columns result_df and  result_years_df
result_Ashwin_df.reset_index(drop=True, inplace=True)
result_years_df.reset_index(drop=True, inplace=True)
result_Ashwin = pd.concat([result_years_df, result_Ashwin_df], axis=1)
result_Ashwin = result_Ashwin.iloc[:,[-2,-1]]

# Add "#" symbol in front of missing values in 'years' column
result_Ashwin["#years"] = result_Ashwin.apply(lambda x: "#"+str(x["#years"]) if pd.isna(x["Ashwin"]) else x["#years"], axis=1)

#export to text file
result_Ashwin.to_csv('Ashwin_average.txt', sep=' ', index=False)

# For Kartik
result_Kartik_df = result_df[["Kartik"]]

#append these two columns result_df and  result_years_df
result_Kartik_df.reset_index(drop=True, inplace=True)
result_years_df.reset_index(drop=True, inplace=True)
result_Kartik = pd.concat([result_years_df, result_Kartik_df], axis=1)
result_Kartik = result_Kartik.iloc[:,[-2,-1]]

# Add "#" symbol in front of missing values in 'years' column
result_Kartik["#years"] = result_Kartik.apply(lambda x: "#"+str(x["#years"]) if pd.isna(x["Kartik"]) else x["#years"], axis=1)

#export to text file
result_Kartik.to_csv('Kartik_average.txt', sep=' ', index=False)

# For Mangsir
result_Mangsir_df = result_df[["Mangsir"]]

#append these two columns result_df and  result_years_df
result_Mangsir_df.reset_index(drop=True, inplace=True)
result_years_df.reset_index(drop=True, inplace=True)
result_Mangsir = pd.concat([result_years_df, result_Mangsir_df], axis=1)
result_Mangsir = result_Mangsir.iloc[:,[-2,-1]]

# Add "#" symbol in front of missing values in 'years' column
result_Mangsir["#years"] = result_Mangsir.apply(lambda x: "#"+str(x["#years"]) if pd.isna(x["Mangsir"]) else x["#years"], axis=1)

#export to text file
result_Mangsir.to_csv('Mangsir_average.txt', sep=' ', index=False)

# For Poush
result_Poush_df = result_df[["Poush"]]

#append these two columns result_df and  result_years_df
result_Poush_df.reset_index(drop=True, inplace=True)
result_years_df.reset_index(drop=True, inplace=True)
result_Poush = pd.concat([result_years_df, result_Poush_df], axis=1)
result_Poush = result_Poush.iloc[:,[-2,-1]]

# Add "#" symbol in front of missing values in 'years' column
result_Poush["#years"] = result_Poush.apply(lambda x: "#"+str(x["#years"]) if pd.isna(x["Poush"]) else x["#years"], axis=1)

#export to text file
result_Poush.to_csv('Poush_average.txt', sep=' ', index=False)

# For Magh
result_Magh_df = result_df[["Magh"]]

#append these two columns result_df and  result_years_df
result_Magh_df.reset_index(drop=True, inplace=True)
result_years_df.reset_index(drop=True, inplace=True)
result_Magh = pd.concat([result_years_df, result_Magh_df], axis=1)
result_Magh = result_Magh.iloc[:,[-2,-1]]

# Add "#" symbol in front of missing values in 'years' column
result_Magh["#years"] = result_Magh.apply(lambda x: "#"+str(x["#years"]) if pd.isna(x["Magh"]) else x["#years"], axis=1)

#export to text file
result_Magh.to_csv('Magh_average.txt', sep=' ', index=False)

# For Falgun
result_Falgun_df = result_df[["Falgun"]]

#append these two columns result_df and  result_years_df
result_Falgun_df.reset_index(drop=True, inplace=True)
result_years_df.reset_index(drop=True, inplace=True)
result_Falgun = pd.concat([result_years_df, result_Falgun_df], axis=1)
result_Falgun = result_Falgun.iloc[:,[-2,-1]]

# Add "#" symbol in front of missing values in 'years' column
result_Falgun["#years"] = result_Falgun.apply(lambda x: "#"+str(x["#years"]) if pd.isna(x["Falgun"]) else x["#years"], axis=1)

#export to text file
result_Falgun.to_csv('Falgun_average.txt', sep=' ', index=False)












