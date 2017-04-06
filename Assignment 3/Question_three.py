
# coding: utf-8

# In[33]:

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


# In[17]:

output_dist={}
for subdir,dirs, files in os.walk(path_to_data):
    #print(files)
    for file in files:
        if file == 'cricket_matches.csv':
            #print(file)
            csv_data1=pd.read_csv(os.path.join(subdir,file))


# ## Making new frame with relevant columns 

# In[18]:

match_details_df = csv_data1[["home","away","winner","innings1","innings1_runs","innings2","innings2_runs"]].copy()
print(match_details_df.head(5))


# ## Getting only those records which are played at home and won the match

# In[19]:

home_winners_df = match_details_df[(match_details_df['home'] == match_details_df['winner'])]


# ### Getting the avg. if they have batted in first innings.  

# In[20]:

home_inning1 = home_winners_df[["home","innings1","innings1_runs"]].copy()
home_inning1 = home_inning1[(home_inning1['home'] == home_inning1['innings1'])]


# In[21]:

home_inning1 = home_inning1.groupby('home', as_index=False)['innings1_runs'].mean()
print(home_inning1.head(5))


# ### getting the aveg. If they batted in second innings 

# In[22]:

home_inning2 = home_winners_df[["home","innings2","innings2_runs"]].copy()
home_inning2 = home_inning2[(home_inning2['home'] == home_inning2['innings2'])]


# In[23]:

home_inning2 = home_inning2.groupby('home', as_index=False)['innings2_runs'].mean()
print(home_inning2.head(5))


# - Combining both results using outer join 

# In[24]:

final_inning_df = pd.merge(home_inning1,home_inning2,on ='home' , how='outer')
final_inning_df.columns = ["home","First_inning_avg","Second_inning_avg"]


# - Calculating final aveg.

# In[27]:

final_inning_df["Total"] = final_inning_df[["First_inning_avg","Second_inning_avg"]].mean(axis=1)


# In[35]:

final_inning_df.drop('First_inning_avg', axis=1, inplace=True)
final_inning_df.drop('Second_inning_avg', axis=1, inplace=True)
final_inning_df["Total"] = final_inning_df["Total"].apply(np.int64)
print(final_inning_df.head(5))


# In[30]:

def save_to_csv():
    if not os.path.exists(homedir+"\\Assignment 3\\Output\\Question3"):
        os.makedirs(homedir+"\\Assignment 3\\Output\\Question3")
    with open(homedir+'\\Assignment 3\\Output\\Question3\\Q3_ouptput.csv', 'w') as myfile:
        myfile.write(final_inning_df.to_csv(index=False))


# In[ ]:

save_to_csv()

