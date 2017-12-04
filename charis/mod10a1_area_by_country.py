
# coding: utf-8

# # MOD10A1 area by country, 2000-2013

# In[1]:

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
get_ipython().magic(u'pylab inline')


# In[9]:

filename = 'Tajikistan.MODIS_persistence_by_day.txt'
df = pd.read_csv( filename, delim_whitespace=True, index_col=0 )
df


# In[8]:

ax = df.plot(style='-o')
ax.legend(bbox_to_anchor=(1.5,1.0))
ax.set(title="MOD10A1", ylabel='MOD10A1 area ($km^2$)' )


# In[ ]:



