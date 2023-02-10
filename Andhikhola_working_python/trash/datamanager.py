
import pandas as pd
from openpyxl import load_workbook


# Create a list of sheet names to read
sheet_names = ["61-62", "62-63", "63-64", "64-65", "65-66", "66-67", "67-68", "68-69", "69-70", "70-71", "71-72", "72-73", "73-74", "74-75", "75-76", "76-77", "77-78", "78-79", "79-80"]

# Read the specified sheets in the Excel file
dfs = pd.read_excel('D:\Andhi Khola and Jhimruk\Andhikhola\Andhikhola61-80.xlsx', sheet_name=sheet_names)

# Create a new dataframe to store all the data
df_final = pd.DataFrame()

# Append the data from each tab to the final dataframe
for sheet, df in dfs.items():
    df_final = df_final.append(df)

# Write the final dataframe to a new tab in the same Excel file
with pd.ExcelWriter('D:\Andhi Khola and Jhimruk\Andhikhola\Andhikhola61-80.xlsx', engine='openpyxl') as writer:
    df_final.to_excel(writer, sheet_name='All_Data', index=False)
