
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


# ### Getting data from CSV file 

# In[3]:

output_dist={}
for subdir,dirs, files in os.walk(path_to_data):
    #print(files)
    for file in files:
        if file == 'vehicle_collisions.csv':
            #print(file)
            csv_data1=pd.read_csv(os.path.join(subdir,file))
print(csv_data1.head(2))


# In[4]:

new_df = csv_data1[["BOROUGH","DATE","VEHICLE 1 TYPE","VEHICLE 2 TYPE","VEHICLE 3 TYPE","VEHICLE 4 TYPE","VEHICLE 5 TYPE"]].copy()


# In[5]:

new_df["DATE"]= pd.to_datetime(new_df.DATE)
new_df["YEAR"] = new_df.DATE.dt.year
print(new_df.head(5))


# # Inserting 1 in place of vehical name and zero for NaN

# In[6]:

new_df['VEHICLE 1 TYPE'] = new_df['VEHICLE 1 TYPE'].str.replace('.*','1')
new_df['VEHICLE 1 TYPE'] = new_df['VEHICLE 1 TYPE'].fillna(0)

new_df['VEHICLE 2 TYPE'] = new_df['VEHICLE 2 TYPE'].str.replace('.*','1')
new_df['VEHICLE 2 TYPE'] = new_df['VEHICLE 2 TYPE'].fillna(0)

new_df['VEHICLE 3 TYPE'] = new_df['VEHICLE 3 TYPE'].str.replace('.*','1')
new_df['VEHICLE 3 TYPE'] = new_df['VEHICLE 3 TYPE'].fillna(0)

new_df['VEHICLE 4 TYPE'] = new_df['VEHICLE 4 TYPE'].str.replace('.*','1')
new_df['VEHICLE 4 TYPE'] = new_df['VEHICLE 4 TYPE'].fillna(0)

new_df['VEHICLE 5 TYPE'] = new_df['VEHICLE 5 TYPE'].str.replace('.*','1')
new_df['VEHICLE 5 TYPE'] = new_df['VEHICLE 5 TYPE'].fillna(0)

print(new_df.head(5))


# ### Getting only data after 2015

# In[7]:

new_df = new_df[(new_df.YEAR >= 2015)].dropna(subset=["BOROUGH"])
print(new_df.head(5))


# ## Counting total for each column 

# In[8]:

vehical_type1_df = new_df[["BOROUGH"]].copy()
vehical_type1_df["one_vehical_involved"] = new_df["VEHICLE 1 TYPE"].astype(str).astype(int)
vehical_type1_df = pd.DataFrame(vehical_type1_df.groupby("BOROUGH").one_vehical_involved.sum().reset_index())


# In[9]:

vehical_type2_df = new_df[["BOROUGH"]].copy()
vehical_type2_df["two_vehical_involved"] = new_df["VEHICLE 2 TYPE"].astype(str).astype(int)
vehical_type2_df = pd.DataFrame(vehical_type2_df.groupby("BOROUGH").two_vehical_involved.sum().reset_index())


# In[10]:

vehical_type3_df = new_df[["BOROUGH"]].copy()
vehical_type3_df["three_vehical_involved"] = new_df["VEHICLE 3 TYPE"].astype(str).astype(int)
vehical_type3_df = pd.DataFrame(vehical_type3_df.groupby("BOROUGH").three_vehical_involved.sum().reset_index())


# In[11]:

vehical_type4_df = new_df[["BOROUGH"]].copy()
vehical_type4_df["four_vehical_involved"] = new_df["VEHICLE 4 TYPE"].astype(str).astype(int)
vehical_type4_df = pd.DataFrame(vehical_type4_df.groupby("BOROUGH").four_vehical_involved.sum().reset_index())


# In[12]:

vehical_type5_df = new_df[["BOROUGH"]].copy()
vehical_type5_df["five_vehical_involved"] = new_df["VEHICLE 5 TYPE"].astype(str).astype(int)
vehical_type5_df = pd.DataFrame(vehical_type5_df.groupby("BOROUGH").five_vehical_involved.sum().reset_index())


# ## Merging all dataframes to get single data frame

# In[13]:

final_df = pd.merge(vehical_type1_df,vehical_type2_df,on ='BOROUGH' , how='inner')
final_df.columns = ["BOROUGH","one_vehical_involved","two_vehical_involved"]

final_df = pd.merge(final_df,vehical_type3_df,on ='BOROUGH' , how='inner')
final_df.columns = ["BOROUGH","one_vehical_involved","two_vehical_involved","three_vehical_involved"]

final_df = pd.merge(final_df,vehical_type4_df,on ='BOROUGH' , how='inner')
final_df.columns = ["BOROUGH","one_vehical_involved","two_vehical_involved","three_vehical_involved","four_vehical_involved"]

final_df = pd.merge(final_df,vehical_type5_df,on ='BOROUGH' , how='inner')
final_df.columns = ["BOROUGH","one_vehical_involved","two_vehical_involved","three_vehical_involved","four_vehical_involved","five_vehical_involved"]

#save_to_CSV()
print(final_df.head(2))


# # Subtracting the colums to get exact count

# In[14]:

final_df["four_vehical_involved"] = final_df["four_vehical_involved"] - final_df["five_vehical_involved"]


# In[15]:

final_df["three_vehical_involved"] = (final_df["three_vehical_involved"] - final_df["four_vehical_involved"])-final_df["five_vehical_involved"]


# In[16]:

final_df["two_vehical_involved"] = ((final_df["two_vehical_involved"]-final_df["three_vehical_involved"])-final_df["four_vehical_involved"])-final_df["five_vehical_involved"]                     


# In[17]:

final_df["one_vehical_involved"]=(((final_df["one_vehical_involved"]-final_df["two_vehical_involved"])-final_df["three_vehical_involved"])-final_df["four_vehical_involved"])- final_df["five_vehical_involved"]


# In[ ]:

output_df = final_df
output_df["More_Vehicals_involved"] = output_df["four_vehical_involved"] + output_df["five_vehical_involved"]
output_df.drop('four_vehical_involved', axis=1, inplace=True)
output_df.drop('five_vehical_involved', axis=1, inplace=True)

print(output_df.head(5))


# In[19]:

def save_to_CSV():
    if not os.path.exists(homedir+"\\Assignment 3\\Output\\Question1_part2"):
        os.makedirs(homedir+"\\Assignment 3\\Output\\Question1_part2")
    with open(homedir+'\\Assignment 3\\Output\\Question1_part2\\Q1P2.csv', 'w') as myfile:
        myfile.write(output_df.to_csv(index=False))


# In[ ]:

save_to_CSV()

