import numpy as np
import scipy.stats as stats

np.random.seed(0) # set seed for reproducibility

# Data
data = [677, 384, 272, 353, 608, 605, 457, 304, 355, 343, 444, 833, 147, 147, 185, 185, 136]

# Fit a Normal distribution to the data
mean, std = stats.norm.fit(data)
se = std/np.sqrt(len(data))
print("Normal Distribution:")
print("Mean:", mean)
print("Standard Error:", se)
print("The no of sample:",len(data))
# Fit a Log-Normal (type 2) distribution to the data
params = stats.lognorm.fit(data, floc=0)
mean = np.log(params[2]) + params[0] * params[1]
se = params[1]/np.sqrt(len(data))
print("\nLog-Normal (Type 2) Distribution:")
print("Mean:", np.exp(mean))
print("Standard Error:", se)

# Fit a Log-Normal (type 3) distribution to the data
params = stats.lognorm.fit(np.log(data), floc=0)
mean = np.log(params[2]) + params[0] * params[1]
se = params[1]/np.sqrt(len(data))
print("\nLog-Normal (Type 3) Distribution:")
print("Mean:", np.exp(mean))
print("Standard Error:", se)

# Fit a Gumbel distribution to the data
params = stats.gumbel_r.fit(data, loc=0, scale=1)
mode = params[0] - params[1] * np.euler_gamma
se = params[1]/np.sqrt(len(data))
print("\nGumbel Distribution:")
print("Mode:", mode)
print("Standard Error:", se)

# Fit a Pearson Type III distribution to the data
params = stats.pearson3.fit(data)
mean = params[2]
#se = params[3]/np.sqrt(len(data))
print("\nPearson Type III Distribution:")
print("Mean:", mean)
#print("Standard Error:", se)

# Fit a Log-Pearson Type III distribution to the data
params = stats.johnsonsu.fit(data, floc=0)
a, b, loc, scale = params
mean = a * np.log(scale) + b
se = np.sqrt((1/len(data)) * np.sum(((data - mean)/b)**2))
print("\nLog-Pearson Type III Distribution:")
print("Mean", mean)
print("standard error",se)

