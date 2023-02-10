
import pandas as pd
# This code reads the monthly data from a entire year from the excel file to  calculate monthly average
# Load the excel file as a dataframe, single tab, data are in col B to col M
df = pd.read_excel('Andhikhola_foraverage.xlsx', usecols = "B:M")

# Select the range of cells B7:M38
df = df.iloc[6:, :]

# Calculate the averages for each column
averages = df.mean(axis=0)

# Create a new dataframe to store the averages
averages_df = pd.DataFrame(averages).T

# Save the new dataframe to a new Excel file
averages_df.to_excel('newfile5.xlsx', index=False, header=False)








