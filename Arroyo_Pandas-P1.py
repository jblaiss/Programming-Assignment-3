#!/usr/bin/env python
# coding: utf-8

# Programming Assignment 3

# Experiment 3 - Python Data Analysis (PANDAS)

# Problem 1

# In[1]:


import pandas as pd


# In[2]:


cars = pd.read_csv('cars.csv') #load the corresponding .csv file
cars


# In[4]:


cars.head() #to display the first five rows of the resulting cars


# In[5]:


cars.tail() #to display the last five rows of the resulting cars


# In[ ]:




