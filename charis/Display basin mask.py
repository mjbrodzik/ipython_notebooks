
# coding: utf-8

# In[1]:

get_ipython().magic(u'pylab notebook')
from charistools.readers import read_tile
import glob
import numpy as np


# In[2]:

import matplotlib.pyplot as plt


# In[3]:

get_ipython().magic(u'cd /Users/brodzik/projects/CHARIS/basins/basin_MODIS_tiles')


# In[4]:

list = glob.glob("GA_Karnali*tif")
list


# In[7]:

for file in list:
    data = read_tile(filename=file)
    print(np.shape(data))
    fig, ax = plt.subplots()
    ax.imshow(data, cmap="Greys", vmin=np.amin(data), vmax=np.amax(data), interpolation='None')
    ax.set_title(file)
    plt.axis('off')


# In[6]:

fig, ax = plt.subplots()
ax.imshow(data, cmap="Greys", vmin=np.amin(data), vmax=np.amax(data), interpolation='None')
ax.set_title(file)
plt.axis('off')


# In[ ]:



