#!/usr/bin/env python
# coding: utf-8

# # Day5HW_Muhammad Noorrosyid Sulaksono

# ### 1) Create the following Pandas DataFrame
import pandas as pd
import numpy as np

# Create dataframe
df = pd.DataFrame({
    "name": ["Anna", "Dane", "David", "Kevin", "Joe", "Rose"],
    "weight": [45.2,50.5,62.1,64.0,59.0,np.nan],
    "height": [155, 160, 162, 170, 167,159],
    "birth_year":[2000,1997,1996,1987,1998,2003],
    "gender":["female", "male", "male", "male", "male", "female"],
    "city":["New York", "Chicago", "Austin", "New York",np.nan,"New York"]
    })
df


# ### 2) Print the basic DataFrame info
# Dataframe info
df.info()


# ### 3) Print the basic statistics information for numerical columns
# Basic statistics information
df.describe()

# ### 4) Reorder the columns to match with the following Pandas DataFrame
# Reorder the columns to ('name','birth_year','height','weight','city','gender')
df = df[['name','birth_year','height','weight','city','gender']]
df

# ### 5) Print all rows that match either of the following conditions:
# - Men that born after the year 1996
# - Women with height > 157 

# Men that born after the year 1996 or Women with height > 157
df[((df['gender'] == 'male') & (df['birth_year']>1996)) | ((df['gender'] == 'female') & (df['height']>157))]

# ### 6) Fill NaN of weight with mean of the gender and fill NaN of city with mode
df.isnull().sum()

# NaN of weight with mean of the female
df['weight'] = df['weight'].fillna((df['weight']).head(1).mean())
df

# fill NaN of city with mode
df['city'] = df['city'].fillna((df['city']).mode()[0])
df

# ### 7) Check outliers of weight and remove if any
# Z-score for check outliers
import scipy.stats as stats
df[(np.abs(stats.zscore(df["weight"])) >= 3)] #there is no outliers in weight's column


# In[110]:


# IQR
q1 = df["weight"].quantile(0.25)
q3 = df["weight"].quantile(0.75)

iqr = q3-q1 #Interquartile range
fence_low  = q1-1.5*iqr
fence_high = q3+1.5*iqr

df.loc[(df["weight"] < fence_low) | (df["weight"] > fence_high)] #there is no outliers in weight's column






