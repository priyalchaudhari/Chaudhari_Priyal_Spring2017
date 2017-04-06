
# coding: utf-8

# In[12]:

import os
from os import listdir
from os.path import isfile, join
import glob
import string
import operator
import csv
import pandas as pd
import calendar
import numpy as np


# - path to data directory

# In[13]:

homedir = os.path.expanduser("~")
path_to_data = homedir+"\\Assignment 3\\Data"
print(path_to_data)


# #### Getting data from CSV in to a data frame 

# In[14]:

output_dist={}
for subdir,dirs, files in os.walk(path_to_data):
    #print(files)
    for file in files:
        if file == 'employee_compensation.csv':
            #print(file)
            csv_data1=pd.read_csv(os.path.join(subdir,file))
print(csv_data1.head(2))


# In[15]:

new_df = csv_data1[["Organization Group","Department","Total Compensation"]].copy()
print(new_df.head(2))


# ### counting the total compensation group by organisation group and department 

# In[16]:

mean_df = new_df[["Organization Group","Department","Total Compensation"]].copy()
#demo["Count"]=1
#demo = pd.DataFrame(demo.groupby("Organization Group").COUNT.sum().reset_index())
mean_df = mean_df.groupby(['Organization Group','Department'])['Total Compensation'].mean()
#demo.sort_values(by='mean',ascending=0)
mean_df= pd.DataFrame(mean_df)
print(mean_df.head(5))


# # Sorting each organisation group

# In[17]:

g = mean_df['Total Compensation'].groupby(level=0, group_keys=False)
sorted_df = g.apply(lambda x: x.order(ascending=False))

sorted_df = pd.DataFrame(sorted_df)
print(sorted_df.head(20))


# In[10]:

def save_to_csv():
    if not os.path.exists(homedir+"\\Assignment 3\\Output\\Question2_part1"):
        os.makedirs(homedir+"\\Assignment 3\\Output\\Question2_part1")
    with open(homedir+'\\Assignment 3\\Output\\Question2_part1\\Q2P1_ouptput.csv', 'w') as myfile:
        myfile.write(sorted_df.to_csv())


# In[ ]:

save_to_csv()

