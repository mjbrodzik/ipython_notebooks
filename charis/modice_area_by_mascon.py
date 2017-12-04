
# coding: utf-8

# # MODICE v04 area by GRACE mascon, 2000-2014

# In[1]:

import glob
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
get_ipython().magic(u'pylab inline')


# In[2]:

files = glob.glob("mascons/*area.txt")
files


# In[3]:

import re


# In[4]:

def read_mascon_data(mascon,filename):
    df = pd.read_csv( filename, delim_whitespace=True, index_col=0 )
    df.head()
    df = df[['MODICE_area_km^2','MODICE_NS_km^2']]
    df.columns = [ mascon + '_modice', mascon + '_ns']
    return df


# In[5]:

p = re.compile('MOD44W.([\+\w]+).area')
data = []
for file in files:
    mascon = p.findall(file)
    print "next file: " + file
    df = read_mascon_data( mascon[0], file )
    data.append(df)
df = pd.concat(data, axis=1)


# In[8]:

df


# ## Get all modice columns (except the one with Greenland, since it's so much larger than the rest)

# In[12]:

modice_cols = [col for col in df.columns if 'modice' in col]
modice_cols.remove('Greenland_modice')
df_modice = df[modice_cols]
df_modice


# In[13]:

ns_cols = [col for col in df.columns if '_ns' in col]
ns_cols.remove('Greenland_ns')
df_ns = df[ns_cols]
df_ns


# In[14]:

ax = df_modice.plot( style='-o')
ax.legend(bbox_to_anchor=(1.5,1.0))
ax.set(title="MODICE.v0.4 (1strike) by mascon", ylabel='MODICE area ($km^2$)' )


# In[15]:

ax = df_ns.plot( style='-o')
ax.legend(bbox_to_anchor=(1.5,1.0))
ax.set(title="MODICE.v0.4 (1strike) never_seen by mascon", ylabel='MODICE area ($km^2$)' )


# In[ ]:



