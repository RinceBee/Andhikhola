import numpy as np
import scipy.stats as stats
import pandas as pd

np.random.seed(0) # set seed for reproducibility

# Data
data = [677, 384, 272, 353, 608, 605, 457, 304, 355, 343, 444, 833, 147, 147, 185, 185, 136]

# Fit a normal distribution to the data
mean, std = stats.norm.fit(data)
se1 = std/np.sqrt(len(data))

# Fit a Gumbel distribution to the data
params = stats.gumbel_r.fit(data, loc=0, scale=1)
mode = params[0] - params[1] * np.euler_gamma
se2 = params[1]/np.sqrt(len(data))

# Fit a Log-Normal distribution to the data
params = stats.lognorm.fit(data, floc=0)
mean = np.log(params[2]) + params[0] * params[1]
se3 = params[1]/np.sqrt(len(data))

# Fit a Log-Pearson Type III distribution to the data
params = stats.johnsonsu.fit(data, floc=0)
a, b, loc, scale = params
mean = a * np.log(scale) + b
se4 = np.sqrt((1/len(data)) * np.sum(((data - mean)/b)**2))

# Perform the Kendall's tau test
tau, p_value = stats.kendalltau(data, np.arange(1, len(data) + 1))

# Save the results in an Excel file
df = pd.DataFrame({"Distribution": ["Normal", "Gumbel", "Log-Normal", "Log-Pearson Type III"],
                   "Mean": [mean, mode, np.exp(mean), mean],
                   "Standard Error": [se1, se2, se3, se4],
                   "Kendall's tau": [np.nan, np.nan, np.nan, np.nan],
                   "p-value": [np.nan, np.nan, np.nan, np.nan]})
df.loc[3, ["Kendall's tau", "p-value"]] = tau, p_value


print (mean, mode, np.exp(mean), mean)
print(se1, se2, se3, se4)
print("tau", tau, "p-value",p_value)


#f.to_excel("fit_results.xlsx", index=False)
