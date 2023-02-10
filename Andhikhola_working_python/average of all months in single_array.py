
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Load the excel file as a dataframe
df = pd.read_excel('Andhikhola_foraverage.xlsx', usecols = "B:M")

# Select the range of cells B7:M38
df = df.iloc[6:, :]

# Calculate the averages for each column
averages = df.mean(axis=0)

# Create a new dataframe to store the averages
averages_df = pd.DataFrame(averages).T
# Define the months of the year
months = ["Shrawan", "Bhadra", "Ashwin", "Kartik", "Mangsir", "Poush", "Magh", "Falgun", "Chaitra", "Baishakh", "Jestha", "Ashadh"]

# Insert the months in the first row of the DataFrame
averages_df.columns = months

# Save the new dataframe to a new Excel file
#averages_df.to_excel('newfile6.xlsx', index=False, header=True)

averages_df = averages_df[["Chaitra", "Baishakh", "Jestha", "Ashadh", "Shrawan", "Bhadra", "Ashwin", "Kartik", "Mangsir", "Poush", "Magh", "Falgun"]]
averages = averages_df.mean(axis=0)
averages.plot(kind='line', marker="D")
plt.xlabel("Months")
plt.ylabel("Discharge (m3/s)")
plt.title("Mean monthly flow of 2061/62")
plt.savefig("hydrograph_1.png")
plt.show()





