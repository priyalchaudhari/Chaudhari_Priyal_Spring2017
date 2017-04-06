
# coding: utf-8

# In[1]:

import os
from os import listdir
from os.path import isfile, join
import glob
import string
import operator
import csv
import pandas as pd
import calendar


# In[2]:

homedir = os.path.expanduser("~")
path_to_data = homedir+"\\Assignment 3\\Data"
print(path_to_data)


# In[3]:

output_dist={}
for subdir,dirs, files in os.walk(path_to_data):
    #print(files)
    for file in files:
        if file == 'vehicle_collisions.csv':
            #print(file)
            csv_data=pd.read_csv(os.path.join(subdir,file))


# ## Extracting year and month from date column 

# In[5]:

csv_data["DATE"] = pd.to_datetime(csv_data.DATE)
csv_data["MONTH"] = csv_data.DATE.dt.month
csv_data["MONTH"] = csv_data["MONTH"].apply(lambda x: calendar.month_abbr [x])
csv_data["YEAR"] = csv_data.DATE.dt.year
print(csv_data.head(2))


# ## Getting the count for MANHATTAN & NYC monthwise 

# In[6]:

csv_data["COUNT"] = 1
Manhattan_df = pd.DataFrame(csv_data[(csv_data.YEAR == 2016) & (csv_data.BOROUGH == "MANHATTAN")].groupby("MONTH").COUNT.sum().reset_index())


# In[7]:

NYC_df = pd.DataFrame(csv_data[(csv_data.YEAR == 2016)].groupby("MONTH").COUNT.sum().reset_index())
print(NYC_df.head(2))


# ## Merging data frame to get the data in single frame 

# In[8]:

total_df = pd.merge(Manhattan_df, NYC_df , on ='MONTH' , how='inner')
total_df.columns = ["MONTH","MANHATTAN","NEWYORK"]
print(total_df.head(2))


# ## Calculating the percentage 

# In[11]:

total_df["Percentage"] = (total_df.MANHATTAN / total_df.NEWYORK)*100
print(total_df.head(2))


# In[10]:

def save_to_CSV():
    if not os.path.exists(homedir+"\\Assignment 3\\Output\\Question1_part1"):
        os.makedirs(homedir+"\\Assignment 3\\Output\\Question1_part1")
    with open(homedir+'\\Assignment 3\\Output\\Question1_part1\\Q1P1.csv', 'w') as myfile:
        myfile.write(total_df.to_csv(index=False))


# In[ ]:

save_to_CSV()

