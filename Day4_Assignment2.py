#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Python program to find the largest among three numbers

# Taking input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Checking the largest number
if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3

# Displaying the result
print(f"The largest number is {largest}")

'''OUTPUT
Enter first number: 4
Enter second number: -6
Enter third number: 0.1
The largest number is 4.0
'''


# In[ ]:




