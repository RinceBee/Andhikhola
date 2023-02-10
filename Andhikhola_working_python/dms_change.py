# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 15:57:08 2023

@author: kumar
"""

import pandas as pd
import re

# Read the Excel file into a pandas DataFrame
df = pd.read_excel('dms.xlsx')

if 'DMS' in df.columns:
    # Define a function to convert the DMS format to separate columns
    def dms_to_decimal(dms):
        # Remove any spaces before the minute and second symbols
        dms = dms.replace("”", "\"")
        dms_parts = dms.split("°")
        degrees = int(dms_parts[0])
        dms_parts = dms_parts[1].split("'")
        minutes = int(dms_parts[0])
        dms_parts = dms_parts[1].split("\"")
        seconds = int(dms_parts[0])

        decimal = degrees + (minutes / 60) + (seconds / 3600)
        return decimal

    # Apply the function to the relevant column in the DataFrame
    df['Decimal'] = df['DMS'].apply(dms_to_decimal)

    # Write the DataFrame to a new Excel file
    df.to_excel('output3.xlsx', index=False)
else:
    print("DMS column is not available in the dataframe.")

