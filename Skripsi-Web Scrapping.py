#!/usr/bin/env python
# coding: utf-8

# ## Importing libraries

# In[1]:


import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


# ## Read website url

# In[2]:


url = 'https://dibi.bnpb.go.id/xdibi2'
file = pd.read_html(url)


# In[3]:


result = file[0]
result.head()


# In[4]:


next_page = '?pr=&kb=&jn=&th=&bl=&tb=2&st=3&kf=0&'


# In[5]:


for i in range(1,4566):
    if i == 1:
        print(url)
    else:
        print(url+next_page+'start='+str((i-2) * 10)+'&start='+str(((i-2) * 10) + 10))


# In[6]:


cols = [i for i in result.columns]


# ## Get the Tabel Column

# In[7]:


data = pd.DataFrame(columns=cols)
data


# ## Get the url every pages

# In[8]:


pages = []

for i in range(1,4566):
    if i == 1:
        pages.append(url)
    else:
        pages.append(url+next_page+'start='+str((i-2) * 10)+'&start='+str(((i-2) * 10) + 10))

pages


# In[9]:


length = len(pages)
length


# In[20]:


for x in range(length):
    scraped = pd.read_html(pages[x])
    data = pd.concat((data, scraped[0]) , axis=0)

data


# In[21]:


data.head()


# In[22]:


data.to_excel('bencana.xlsx',index = False)


# In[23]:


data = data.reset_index()


# In[24]:


data


# In[27]:


data.drop(columns='index')


# ## Drop Data Non Jawa Barat

# In[76]:


data = pd.read_excel('bencana.xlsx')


# In[77]:


data


# In[78]:


data = data.rename({'⫷KIB⫸': 'KIB'}, axis=1)


# In[79]:


data


# In[80]:


word = 'Jawa Barat'

df_jabar = data[data["Wilayah"].str.contains(word)]


# In[81]:


df_jabar


# In[82]:


df_jabar


# In[83]:


df_jabar = df_jabar.drop(['Detail','Unnamed: 5'], axis=1)


# In[88]:


df_jabar


# In[89]:


df_jabar['KIB'] = df_jabar['KIB'].astype(str)


# In[90]:


df_jabar['Tanggal'] = df_jabar['KIB'].str[7:15]


# In[91]:


df_jabar['Tanggal'] = (df_jabar['KIB'].str[13:15] + '/' + df_jabar['KIB'].str[11:13] + '/' + df_jabar['KIB'].str[7:11])


# In[92]:


df_jabar


# In[93]:


df_jabar['Tanggal'] = pd.to_datetime(df_jabar['Tanggal'], format= '%d/%m/%Y')


# In[94]:


df_jabar.reset_index(inplace = True)


# In[95]:


df_jabar


# In[96]:


df_jabar.drop(['index'], axis=1, inplace=True)


# In[97]:


df_jabar


# In[98]:


df_jabar['Indeks'] = df_jabar['KIB'].str[15]


# In[99]:


df_jabar


# In[100]:


df_jabar['Kode Bencana'] = df_jabar['KIB'].str[4:7]


# In[101]:


df_jabar


# In[102]:


df_jabar['Kode Kabupaten/Kota'] = df_jabar['KIB'].str[2:4]


# In[103]:


df_jabar


# In[104]:


df_jabar = df_jabar[["KIB","Tanggal","Wilayah","Kode Kabupaten/Kota","Kejadian","Kode Bencana","Indeks"]]


# In[105]:


condition = ['101','102','103','105','107','108']

mask = df_jabar["Kode Bencana"].isin(condition)
df_jabar = df_jabar[mask]


# In[108]:


df_jabar.reset_index(inplace=True)


# In[110]:


df_jabar.drop(['index'], axis=1, inplace=True)


# In[111]:


df_jabar


# ## Export results to Excel and CSV

# In[113]:


df_jabar.to_excel('bencana_jabar.xlsx',index=False)
df_jabar.to_csv('bencana_jabar.csv',index=False)

