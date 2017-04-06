
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
import re


# In[2]:

homedir = os.path.expanduser("~")
path_to_data = homedir+"\\Assignment 3\\Data"
print(path_to_data)


# In[3]:

output_dist={}
for subdir,dirs, files in os.walk(path_to_data):
    #print(files)
    for file in files:
        if file == 'movies_awards.csv':
            #print(file)
            csv_data1=pd.read_csv(os.path.join(subdir,file))


# In[4]:

new_df = csv_data1[["Title","Awards"]].copy()
print(new_df.head(10))


# ## Removing NaN

# In[5]:

new_df=new_df.dropna(subset=['Awards'])
print(new_df.head(10))


# # Using REGX  separating the count

# In[6]:

new_df["Awards_won"] = new_df["Awards"].apply(lambda x : (re.findall(r"(\d+) win", x))) #find all sentences with pattern 2 win or 3 win
new_df["Awards_won"] = new_df["Awards_won"].apply(lambda x : [0] if len(x)==0 else x)  # getting the 0th element of array
new_df["Awards_won"] = new_df["Awards_won"].apply(lambda x : list(map(int,x))[0])     #Converting in to integer

# Doing this for all award categories with respective pattern 

new_df["Awards_Nominated"] = new_df["Awards"].apply(lambda x : (re.findall(r"(\d+) nominations", x)))
new_df["Awards_Nominated"] = new_df["Awards_Nominated"].apply(lambda x : [0] if len(x)==0 else x)
new_df["Awards_Nominated"] = new_df["Awards_Nominated"].apply(lambda x : list(map(int,x))[0])

new_df["Golden_glob_awards_won"] = new_df["Awards"].apply(lambda x : (re.findall(r"Won (\d+) Golden ", x)))
new_df["Golden_glob_awards_won"] = new_df["Golden_glob_awards_won"].apply(lambda x : [0] if len(x)==0 else x)
new_df["Golden_glob_awards_won"] = new_df["Golden_glob_awards_won"].apply(lambda x : list(map(int,x))[0])

new_df["Golden_glob_awards_Nominated"] = new_df["Awards"].apply(lambda x : (re.findall(r"Nominated for (\d+) Golden ", x)))
new_df["Golden_glob_awards_Nominated"] = new_df["Golden_glob_awards_Nominated"].apply(lambda x : [0] if len(x)==0 else x)
new_df["Golden_glob_awards_Nominated"] = new_df["Golden_glob_awards_Nominated"].apply(lambda x : list(map(int,x))[0])


# In[7]:

new_df["Oscar_awards_Nominated"] = new_df["Awards"].apply(lambda x : (re.findall(r"Nominated for (\d+) Oscar", x)))
new_df["Oscar_awards_Nominated"] = new_df["Oscar_awards_Nominated"].apply(lambda x : [0] if len(x)==0 else x)
new_df["Oscar_awards_Nominated"] = new_df["Oscar_awards_Nominated"].apply(lambda x : list(map(int,x))[0])


# In[8]:

new_df["Oscar_Won"] = new_df["Awards"].apply(lambda x : (re.findall(r"Won (\d+) Oscar", x)))
new_df["Oscar_Won"] = new_df["Oscar_Won"].apply(lambda x : [0] if len(x)==0 else x)
new_df["Oscar_Won"] = new_df["Oscar_Won"].apply(lambda x : list(map(int,x))[0])


# In[9]:

new_df["Prime_awards_nominated"] = new_df["Awards"].apply(lambda x : (re.findall(r"Nominated for (\d+) Primetime", x)))
new_df["Prime_awards_nominated"] = new_df["Prime_awards_nominated"].apply(lambda x : [0] if len(x)==0 else x)
new_df["Prime_awards_nominated"] = new_df["Prime_awards_nominated"].apply(lambda x : list(map(int,x))[0])


# In[10]:

new_df["Prime_awards_won"] = new_df["Awards"].apply(lambda x : (re.findall(r"Won (\d+) Primetime", x)))
new_df["Prime_awards_won"] = new_df["Prime_awards_won"].apply(lambda x : [0] if len(x)==0 else x)
new_df["Prime_awards_won"] = new_df["Prime_awards_won"].apply(lambda x : list(map(int,x))[0])


# In[11]:

new_df["BAFTA_awards_nominated"] = new_df["Awards"].apply(lambda x : (re.findall(r"Nominated for (\d+) BAFTA", x)))
new_df["BAFTA_awards_nominated"] = new_df["BAFTA_awards_nominated"].apply(lambda x : [0] if len(x)==0 else x)
new_df["BAFTA_awards_nominated"] = new_df["BAFTA_awards_nominated"].apply(lambda x : list(map(int,x))[0])


# In[12]:

new_df["BAFTA_awards_won"] = new_df["Awards"].apply(lambda x : (re.findall(r"Won (\d+) BAFTA", x)))
new_df["BAFTA_awards_won"] = new_df["BAFTA_awards_won"].apply(lambda x : [0] if len(x)==0 else x)
new_df["BAFTA_awards_won"] = new_df["BAFTA_awards_won"].apply(lambda x : list(map(int,x))[0])


# # Adding all categories to get Total win and total nominated 

# In[13]:

new_df["Awards_won"] = ((((new_df["Awards_won"] + new_df["Golden_glob_awards_won"]) + new_df["Oscar_Won"]) + new_df["Prime_awards_won"]) + new_df["BAFTA_awards_won"])
new_df["Awards_Nominated"] = ((((new_df["Awards_Nominated"] + new_df["Golden_glob_awards_Nominated"]) + new_df["Oscar_awards_Nominated"]) + new_df["Prime_awards_nominated"]) + new_df["BAFTA_awards_nominated"])
print(new_df.head(5))


# # Writing data into csv file 

# In[14]:

def save_to_csv():
    if not os.path.exists(homedir+"\\Assignment 3\\Output\\Question4"):
        os.makedirs(homedir+"\\Assignment 3\\Output\\Question4")
    with open(homedir+'\\Assignment 3\\Output\\Question4\\Q4_ouptput.csv', 'w') as myfile:
        myfile.write(new_df.to_csv(index=False))


# In[15]:

save_to_csv()


# In[ ]:



