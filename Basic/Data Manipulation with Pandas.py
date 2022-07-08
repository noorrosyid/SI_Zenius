#!/usr/bin/env python
# coding: utf-8

# # Day6HW_Muhammad Noorrosyid Sulaksono
# ### Assignment Python for Data Analysis: Data Manipulation with Pandas

# #### 1) Create the following Pandas DataFrame

import pandas as pd
import numpy as np

# Create dataframe
df1 = pd.DataFrame({
    "name": ["Anna", "Dane", "David", "Kevin", "Joe", "Rose"],
    "weight": [45.2,50.5,62.1,64.0,59.0,np.nan],
    "height": [155, 160, 162, 170, 167,159],
    "birth_year":[2000,1997,1996,1987,1998,2003],
    "gender":["female", "male", "male", "male", "male", "female"],
    "city":["New York", "Chicago", "Austin", "New York",np.nan,"New York"]
    })


# #### 2) Create another Pandas DataFrame as the following and merge it with the previous DataFrame (key=name and nick name). Make sure that no rows are missing from the original DataFrame
#create another dataframe
df2 = pd.DataFrame({
    'nick_name':['Anna','David','Dane','Rose'],
    'full_name':['Anna Levis', 'David John','Dane Sebastian', 'Rose Kimberly']
    })


# #### 3) Drop nick_name column and fill null values in the full_name from the merged DataFrame with their original name column.
# merged df2 into df1 and drop nick_name column
df3 = df1.merge(df2, how = 'left', left_on = 'name', right_on = 'nick_name').drop(columns = 'nick_name')
df3 = df3[['name','full_name','weight','height','birth_year','gender','city']]
df3


# #### 4) Create a new ‘bmi’ column calculated based on the following formula
#                   BMI (kg/m^2) = weight / (height/100)^2
df3['bmi'] = (df3['weight']/(df3['height']/100)**2)


# #### 5) Create a new ‘bmi_class’ column following the definition in the table below.
#create function of bmi_class
def bmi_class (bmi):
    if bmi<18.5:
        return 'Underweight'
    elif (18.5<=bmi<25):
        return 'Normal Weight'
    elif (25<=bmi<30):
        return 'Overweight'
    elif (30<=bmi<35):
        return 'Obesity Class 1'
    elif (35<=bmi<40):
        return 'Obesity Class 2'
    elif (bmi>=40):
        return 'Obesity Class 3'

#put the function before and create new column of df3 called bmi_class
df3['bmi_class'] = df3.apply(lambda x: bmi_class(x['bmi']), axis = 1)

df3





