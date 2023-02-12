# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 12:34:14 2023

@author: kumar
"""

import numpy as np
import scipy.stats as stats

np.random.seed(0) # set seed for reproducibility

# Data
data = [2.7775, 3.45, 4.445333333, 3.254, 1.665333333, 2.6501232, 3.313763226, 3.117220654,
        4.040232099, 1.928774202, 3.877515738, 4.311600621, 6.486357118, 6.589914754, 3.182863686, 4.800898001]

# Perform the Kendall's tau test
tau, p_value = stats.kendalltau(data, np.arange(1, 17))


print("Kendall's tau:", tau)
print("p-value:", p_value)
