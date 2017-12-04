
# coding: utf-8

# # MODICE v04 area by country, 2000-2014

# In[1]:

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
get_ipython().magic(u'pylab inline')


# In[62]:

filename = 'modice_v4_3strikes_by_country_by_yr.txt'
df3 = pd.read_csv( filename, delim_whitespace=True, index_col=0 )
df3


# ## Reorder columns, descending area
# Use the first row of data to order the columns in descending area order

# In[63]:

sorted_col_index = df3.ix[df3.first_valid_index()].argsort()[::-1]
print sorted_col_index
df3 = df3[sorted_col_index]
df3


# ## Get 1 and 2strike data also:

# In[64]:

filename = 'modice_v4_2strikes_by_country_by_yr.txt'
df2 = pd.read_csv( filename, delim_whitespace=True, index_col=0 )
df2 = df2[sorted_col_index]
filename = 'modice_v4_1strikes_by_country_by_yr.txt'
df1 = pd.read_csv( filename, delim_whitespace=True, index_col=0 )
df1 = df1[sorted_col_index]


# In[65]:

print df1
print df2


# In[66]:

my_colors = list(['b','g','r','c','m'])
fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, figsize=(10,10))

df3.plot(ax=axes[0], style='-o', color=my_colors)
axes[0].legend(bbox_to_anchor=(1.3,1.0))
axes[0].set(title="MODICE(3strike) by Country", ylabel='MODICE area ($km^2$)' )

df2.plot(ax=axes[1], style='-o', color=my_colors)
axes[1].legend(bbox_to_anchor=(1.3,1.0))
axes[1].set(title="MODICE(2strike) by Country", ylabel='MODICE area ($km^2$)' )

df1.plot(ax=axes[2], style='-o', color=my_colors)
axes[2].legend(bbox_to_anchor=(1.3,1.0))
axes[2].set(title="MODICE(1strike) by Country", ylabel='MODICE area ($km^2$)' )


# ## Just look at detail on three lowest lines:

# In[67]:

subdf3 = df3[['Kazakhstan','Uzbekistan','Turkmenistan']]
subdf2 = df2[['Kazakhstan','Uzbekistan','Turkmenistan']]
subdf1 = df1[['Kazakhstan','Uzbekistan','Turkmenistan']]


# In[68]:

my_sub_colors = my_colors[2:]

fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, figsize=(10,10))

subdf3.plot(ax=axes[0], style='-o', color=my_sub_colors)
axes[0].legend(bbox_to_anchor=(1.3,1.0))
axes[0].set(title="MODICE(3strike) by Country", ylabel='MODICE area ($km^2$)' )

subdf2.plot(ax=axes[1], style='-o', color=my_sub_colors)
axes[1].legend(bbox_to_anchor=(1.3,1.0))
axes[1].set(title="MODICE(2strike) by Country", ylabel='MODICE area ($km^2$)' )

subdf1.plot(ax=axes[2], style='-o', color=my_sub_colors)
axes[2].legend(bbox_to_anchor=(1.3,1.0))
axes[2].set(title="MODICE(1strike) by Country", ylabel='MODICE area ($km^2$)' )


# In[ ]:



