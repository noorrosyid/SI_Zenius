#!/usr/bin/env python
# coding: utf-8

# A company wants to run a new campaign to increase the transactions’ amount of its product.
# Before running the actual campaign to the whole customers, the company wants to know the 
# campaign’s effectiveness in their 30 days transactions’ amount.
# The average of transactions’ amount before the campaign is $100.
# The company ran a testing on 20 customers and gathered their transactions’ amount in the next 30 
# days after the campaign. The data is stored in this table below.
# Run a t-test analysis on the transactions’ amount average (with alpha = 5%). 

# Instructions:
# - Define H0 and H1
# - Follow the steps to do T-Test
# - Conclude the result of the campaign testing


import numpy as np
import pandas as pd
import scipy.stats as stats


data = [100,150,50,100,130,120,100,110,75,65,150,120,50,100,100,140,90,150,50,90]
data = np.array(data)  #change the type of data from list to array


# ### Define H0 and H1
# h0 = $100
# h1 > $100


#perform one sample t-test
stats.ttest_1samp(a=data, popmean=100)

#T-Test one tailed test
#find the cricital region
stats.t.ppf(1-(0.05), 19)
#cricital region = 1.729132811521367, t = 0.2731657711666385

# Using P-Value
# Because we use P-value one tailed test:
pvalue = 0.787672894169515
pvalue = pvalue/2
#p-value = 0.3938364470847575, alpha = 0.05

# ### Conclusion
# - t < cricital Region , We reject H1
# - p-value > alpha, We reject H1
# So, the campaign is not effective to increase the transactions’ amount of its product.
