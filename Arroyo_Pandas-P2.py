#!/usr/bin/env python
# coding: utf-8

# Programming Assignment 3

# Experiment 3 - Python Data Analysis (PANDAS)

# Problem 2

# In[3]:


import pandas as pd


# In[4]:


#dataframe

cars = pd.read_csv('cars.csv') #load the corresponding .csv file
cars


# In[11]:


#filters the dataframe to only display the first five rows with odd numbered columns

cars.iloc[:5, ::2] 


# In[6]:


#filters the dataframe to display the row that contains the Mazda RX4 Model

cars.loc[cars['Model']=='Mazda RX4']


# In[7]:


#filters the dataframe to only display the cyl of the Camaro Z28 model 

cars.loc[(cars['Model']=='Camaro Z28'),['cyl']]


# In[8]:


#filters the dataframe to only display what the cyl and gear each model has

cars.loc[[1, 28, 18], ['Model', 'cyl', 'gear']] 


# In[ ]:




