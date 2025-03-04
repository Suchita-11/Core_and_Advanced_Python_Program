#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Python program to check if a number is positive, negative, or zero

# Taking input from the user
num = float(input("Enter a number: "))

# Checking the number
if num > 0:
    print(f"{num} is a positive number.")
elif num < 0:
    print(f"{num} is a negative number.")
else:
    print("The number is zero.")
    
'''OUTPUT
Enter a number: 5
5.0 is a positive number.

Enter a number: -8
-8.0 is a negative number.

Enter a number: 0
The number is zero.
'''


# In[ ]:




