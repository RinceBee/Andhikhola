# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 12:05:40 2023

@author: kumar
"""

import pandas as pd

# read the excel file
data = pd.read_excel("Daily_discharge.xlsx")

# select rows and columns
data_list = data.iloc[ 1:30, 1:13 ]

# rename columns
data_list.columns = ["values", "Date"]

# insert the data_list dataframe to the 9th column
data.insert(loc=8, column='new_column', value=data_list)

# save the updated dataframe to the same excel file
data.to_excel("Daily_discharge_25.xlsx", index=False, header=True)

