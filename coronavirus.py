#!/usr/bin/env python
# coding: utf-8

# In[30]:


import geopandas as gpd
import pandas as pd
import requests
import mapclassify
import matplotlib.pyplot as plt
import re


# In[2]:


r = requests.get('https://www.worldometers.info/coronavirus').text
r = re.sub(r'<.*?>', lambda g: g.group(0).upper(), r)
data = pd.read_html(r)


# In[3]:


for data_cases in data:
    print(data_cases)


# In[4]:


data_cases = data_cases[['Country,Other','TotalCases']]


# In[5]:


data_cases.groupby('Country,Other')['TotalCases'].sum()


# In[6]:


world_data = gpd.read_file('World_Countries__Generalized_.shp')
world_data.plot()


# In[7]:


world_data.columns


# In[8]:


for items in world_data['COUNTRY'].tolist():
    print (items)


# In[9]:


for items in data_cases['Country,Other'].tolist():
    if items not in world_data['COUNTRY'].tolist():
        print(items)
    else:
        pass


# In[10]:


world_data.replace('South Korea', 'S. Korea',inplace=True)
world_data.replace('United Arab Emirates', 'UAE',inplace=True)
world_data.replace('United States', 'USA',inplace=True)
world_data.replace('United Kingdom', 'UK',inplace=True)
world_data.replace('Central African Republic', 'CAR',inplace=True)
world_data.replace('Russian Federation','Russia',inplace=True)
world_data.replace('Congo DRC','DRC',inplace=True)
world_data.replace('Czech Republic','Czechia',inplace=True)
world_data.replace("Côte d'Ivoire","Ivory Coast",inplace=True)
world_data.replace('Curacao','Curaçao',inplace=True)                 
world_data.replace('Palestinian territory','Palestine',inplace=True)
world_data.replace('Faroe Islands','Faeroe Islands',inplace=True)
world_data.replace('Turks and Caicos Islands','Turks and Caicos',inplace=True)


# In[11]:


world_data.head()


# In[12]:


data_cases.rename(columns={'Country,Other':'COUNTRY'},inplace=True)


# In[13]:


data_cases.columns


# In[14]:


combined = world_data.merge(data_cases, on = 'COUNTRY', how = 'right')


# In[15]:


ax = combined.plot(figsize=(20,10))
ax =ax.axis('off')


# In[16]:


combined.head(20)


# In[17]:


type(combined)


# In[122]:


combined.to_file(r'combined.shp')


# In[31]:


ax = combined.plot(column='TotalCases',figsize=(20,10),legend=True,legend_kwds={'label':'Casos de Coronavirus por pais','orientation':'horizontal'},cmap='OrRd',scheme='quantiles')
ax = plt.savefig('coronavirus.jpg')
ax.axis('off')


# In[23]:


current_crs = combined.crs


# In[ ]:


combined.plot.bar('TotalCases')


# In[ ]:




