#!/usr/bin/env python
# coding: utf-8

# In[5]:


#importing libraries
import pandas as pds
import numpy as np


# In[6]:


def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# Prompt the user to enter a number
num = int(input("Enter a number: "))

# Call the factorial function and print the result
fact = factorial(num)
print("The factorial of", num, "is", fact)


# In[ ]:




