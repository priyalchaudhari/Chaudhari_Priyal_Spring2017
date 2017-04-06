
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
import numpy as np


# In[2]:

homedir = os.path.expanduser("~")
path_to_data = homedir+"\\Assignment 3\\Data"
print(path_to_data)


# ### Getting the data from CSV 

# In[3]:

output_dist={}
for subdir,dirs, files in os.walk(path_to_data):
    #print(files)
    for file in files:
        if file == 'employee_compensation.csv':
            #print(file)
            csv_data1=pd.read_csv(os.path.join(subdir,file))
print(csv_data1.head(2))


# ### Getting only relevant columns  

# In[4]:

employee_df = csv_data1[["Year Type","Employee Identifier","Job Family","Salaries","Overtime","Total Benefits","Total Compensation"]].copy()
print(employee_df.head(2))


# # getting only Employees for  calender year

# In[5]:

employee_df = employee_df[(employee_df['Year Type'] == 'Calendar')]
print(employee_df.head(5))


# ### Mean of total compansation

# In[6]:

employee_df_total_com = employee_df.groupby('Employee Identifier', as_index=False)['Total Compensation'].mean()
print(employee_df_total_com.head(5))


# ### Calculating mean for total benefits 

# In[7]:

employee_df_total_benifit = employee_df.groupby('Employee Identifier', as_index=False)['Total Benefits'].mean()
print(employee_df_total_benifit.head(5))


# # Joining both frames to get final frame with mean of both columns 

# In[8]:

final_df = pd.merge(employee_df_total_com,employee_df_total_benifit,on ='Employee Identifier' , how='inner')
final_df.columns = ["Employee Identifier","Total Compensation","Total Benefits"]
print(final_df.head(5))


# ### Getting data for employees whos overtime is more than 5% of salaries 

# In[9]:

salaries_df = employee_df[(employee_df['Overtime'] > 0.05*employee_df['Salaries'])]
print(salaries_df.head(5))


# In[10]:

job_family_df = salaries_df[["Job Family","Total Benefits","Total Compensation"]].copy()


# # Calculating the mean of both columns 

# In[11]:

job_family_total_benifits = job_family_df.groupby('Job Family', as_index=False)['Total Benefits'].mean()
print(job_family_total_benifits.head(5))


# In[12]:

job_family_total_comp = job_family_df.groupby('Job Family', as_index=False)['Total Compensation'].mean()
print(job_family_total_comp.head(5))


# ## Joining both data frames 

# In[13]:

final_job_family_df = pd.merge(job_family_total_benifits,job_family_total_comp,on ='Job Family' , how='inner')
final_job_family_df.columns = ["Job Family","Total Benefits","Total Compensation"]
print(final_job_family_df.head(5))


# In[14]:

final_job_family_df["Percentage"] = (final_job_family_df['Total Benefits']/ final_job_family_df['Total Compensation'])*100
print(final_job_family_df.head(20))


# In[20]:

def save_to_pdf():
    if not os.path.exists(homedir+"\\Assignment 3\\Output\\Question2_part2"):
        os.makedirs(homedir+"\\Assignment 3\\Output\\Question2_part2")
    with open(homedir+'\\Assignment 3\\Output\\Question2_part2\\Q2P2_ouptput.csv', 'w') as myfile:
        myfile.write(final_job_family_df.to_csv())


# In[ ]:

save_to_pdf()

