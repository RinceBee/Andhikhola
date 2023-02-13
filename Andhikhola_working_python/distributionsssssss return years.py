# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 17:00:00 2023

@author: kumar
"""

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
q = mean + stats.norm.ppf(1/2) * std
print("Return period for 1 in 2 years:", q)
q = mean + stats.norm.ppf(1/10) * std
print("Return period for 1 in 10 years:", q)
q = mean + stats.norm.ppf(1/20) * std
print("Return period for 1 in 20 years:", q)
q = mean + stats.norm.ppf(1/100) * std
print("Return period for 1 in 100 years:", q)

# Fit a Log-Normal (type 2) distribution to the data
params = stats.lognorm.fit(data, floc=0)
mean = np.log(params[2]) + params[0] * params[1]
se = params[1]/np.sqrt(len(data))
print("\nLog-Normal (Type 2) Distribution:")
print("Mean:", np.exp(mean))
print("Standard Error:", se)
q = np.exp(mean + stats.lognorm.ppf(1/2, params[0], loc=0, scale=params[2]))
print("Return period for 1 in 2 years:", q)
q = np.exp(mean + stats.lognorm.ppf(1/10, params[0], loc=0, scale=params[2]))
print("Return period for 1 in 10 years:", q)
q = np.exp(mean + stats.lognorm.ppf(1/20, params[0], loc=0, scale=params[2]))
print("Return period for 1 in 20 years:", q)
q = np.exp(mean + stats.lognorm.ppf(1/100, params[0], loc=0, scale=params[2]))
print("Return period for 1 in 100 years:", q)

# Fit a Log-Normal (type 3) distribution to the data
params = stats.lognorm.fit(np.log(data), floc=0)
mean = np.log(params[2]) + params[0] * params[1]
se = params[1]/np.sqrt(len(data))
print("\nLog-Normal (Type 3) Distribution:")
print("Mean:", np.exp(mean))
print("Standard Error:", se)
q = np.exp(mean + stats.lognorm.ppf(1/2, params[0], loc=0, scale=np.exp(mean)))
print("Return period for 1 in 2 years:", q)
q = np.exp(mean + stats.lognorm.ppf(1/10, params[0], loc=0, scale=np.exp(mean)))
print("Return period for 1 in 10 years:", q)
q = np.exp(mean + stats.lognorm.ppf(1/20, params[0], loc=0, scale=np.exp(mean)))
print("Return period for 1 in 20 years:", q)
q = np.exp(mean + stats.lognorm.ppf(1/100, params[0], loc=0, scale=np.exp(mean)))
print("Return period for 1 in 100 years:", q)

# Fit a Gumbel distribution to the data
params = stats.gumbel_r.fit(data)
mean = params[0] + params[1] * np.euler_gamma
se = params[1]/np.sqrt(len(data))
print("\nGumbel Distribution:")
print("Mean:", mean)
print("Standard Error:", se)
q = mean - params[1] * np.log(-np.log(1/2))
print("Return period for 1 in 2 years:", q)
q = mean - params[1] * np.log(-np.log(1/10))
print("Return period for 1 in 10 years:", q)
q = mean - params[1] * np.log(-np.log(1/20))
print("Return period for 1 in 20 years:", q)
q = mean - params[1] * np.log(-np.log(1/100))
print("Return period for 1 in 100 years:", q)

# Fit a Pearson Type III distribution to the data
params = stats.pearson3.fit(data)
mean = params[1]
se = params[2]/np.sqrt(len(data))
print("\nPearson Type III Distribution:")
print("Mean:", mean)
print("Standard Error:", se)
q = mean + stats.pearson3.ppf(1/2, params[0], params[1], params[2])
print("Return period for 1 in 2 years:", q)
q = mean + stats.pearson3.ppf(1/10, params[0], params[1], params[2])
print("Return period for 1 in 10 years:", q)
q = mean + stats.pearson3.ppf(1/20, params[0], params[1], params[2])
print("Return period for 1 in 20 years:", q)
q = mean + stats.pearson3.ppf(1/100, params[0], params[1], params[2])
print("Return period for 1 in 100 years:", q)

#
