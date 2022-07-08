#!/usr/bin/env python
# coding: utf-8

# # Day4HW_Muhammad Noorrosyid Sulaksono  

# Create a function called ‘leap_year’ that takes in an integer value (let’s call it x). 
# 
# Your function should:
# 
# - Check if the input integer(x) is a leap year or not. 
# - If the input integer is a leap year, please print out (‘Year x is a leap year’)
# - If the input integer is NOT a leap year:
# - Find out the next leap year after year x, and please print out (‘Year x is not a leap year. The next leap year after x is <give your answer here>’)

# In[3]:


#function to input the year
def input_leap_year(x): 
    return x

#function to calculate the right leap year
def true_leap_year(x): 
    return(int(4-(float(x)%4)+float(x)))

#function to check if the input is a leap year or not, if the input is not a leap year it will be printed the next leap year after the year's input.
def leap_year(x):
    if float(x)%4 == 0:
        print('Year', input_leap_year(x), 'is a leap year.')
    else:
        print('Year', input_leap_year(x), 'is not a leap year. The next leap year after', input_leap_year(x), 'is' , true_leap_year(x))





