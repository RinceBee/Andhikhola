# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 09:55:22 2023

@author: kumar
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load the excel file
df = pd.read_excel('monthy_average_from61-80.xlsx')

# Select the data in the range B7:M38
data = df.iloc[0:13, 1:20]

# Concatenate all columns into a single column
data = pd.concat([data[col] for col in data.columns], axis=0)

# Reset the index
data = data.reset_index(drop=True)
# Save the data to a new Excel file
#data.to_excel('fileee1.xlsx', index=False)


# Create a simple series
#x = np.array([1, 2, 3, 4, 5])
#y = x ** 2

# Plot the series
plt.plot(data)

# Add labels to the axes
plt.ylabel('discharge')
plt.xlabel('time in days from 2061 shrawan 1')


# Display the plot
plt.show()


