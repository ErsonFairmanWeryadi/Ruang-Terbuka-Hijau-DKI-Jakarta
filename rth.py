#!/usr/bin/env python
# coding: utf-8

# In[33]:


import pandas as pd
import numpy as np


# In[34]:


df = pd.read_csv('rth.csv')
df


# In[35]:


#Jenis-Jenis RTH


# In[36]:


jumlah_rth = df['jenis'].value_counts()
jumlah_rth


# In[37]:


#Persebaran RTH Perkotamadya


# In[38]:


per_kotamadya = df['kotamadya'].value_counts()
per_kotamadya


# In[39]:


#Persebaran RTH Perkecamatan


# In[40]:


per_kecamatan = df['kecamatan'].value_counts()
per_kecamatan


# In[41]:


#RTH dengan luas Terbesar


# In[42]:


df_terluas = df[df['luas'] == df['luas'].max()]
df_terluas


# In[43]:


#Menghitung Luas RTH Perkotamadya(Satuan Meter Persegi)


# In[44]:


totalluas_perkotamadya = df.groupby('kotamadya')['luas'].sum()
totalluas_perkotamadya


# In[45]:


# menghitung total luas jenis RTH 


# In[46]:


totalluas_jenis_RTH = df.groupby('jenis')['luas'].sum()
totalluas_jenis_RTH


# In[48]:


totalluas_perkotamadya = df.groupby('kotamadya')['luas'].sum()
totalluas_perkotamadya


# In[ ]:




