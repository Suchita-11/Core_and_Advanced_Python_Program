#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Python program to check if a year is a leap year or not

year = int(input("Enter a year: "))

# Check if the year is divisible by 4 but not by 100, or if it is divisible by 400
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
    

''' OUTPUT
Enter a year: 2028
2028 is a leap year.

Enter a year: 2025
2025 is not a leap year.
'''


# In[ ]:




