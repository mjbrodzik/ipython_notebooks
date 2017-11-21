
# coding: utf-8

# In[27]:

get_ipython().magic(u'pylab inline')
import matplotlib.pyplot as plt
import numpy as np

from charistools.readers import read_tile
pylab.rcParams['figure.figsize'] = (10.0, 8.0)


# In[28]:

get_ipython().magic(u'cd /Users/brodzik/projects/CHARIS/elevation_data/SRTMGL3_version2/')
get_ipython().magic(u'ls')


# In[29]:

datav2= read_tile('CHARIS_DEM.v0.2.h23v05.tif')


# In[30]:

np.amin(datav2), np.amax(datav2), np.amax(datav2[datav2 != 32767])


# In[31]:

datav2.shape


# In[32]:

get_ipython().magic(u'cd /Users/brodzik/projects/CHARIS/elevation_data/SRTMGL3/')
get_ipython().magic(u'ls')


# In[33]:

data= read_tile('SRTMGL3.v0.1.h23v05.tif')
np.amin(data), np.amax(data), np.amin(data[data != -32768])


# In[40]:

fig, ax = plt.subplots(1,2)
ax[0].imshow(data, cmap=plt.cm.gray, vmin=170, vmax=8000, interpolation='None')
ax[0].set_title('SRTMGL3 (v1)')
ax[1].imshow(datav2, cmap=plt.cm.gray, vmin=170, vmax=8000, interpolation='None')
ax[1].set_title('CHARIS_DEM (v2)')
plt.axis('off')
fig.savefig('/Users/brodzik/tmp/SRTMGL3_vs_CHARIS_DEMv2.png')


# In[35]:

diff = datav2.astype('float') - data.astype('float')
diff[data == -32768] = 0
diff[datav2 == 32767] = 0


# In[36]:

print np.amin(diff)
print np.amax(diff)


# In[ ]:

print(data[1:2,:])


# In[45]:

test = np.array([3.2, 5.6, 2.0, 4.4])
test


# In[46]:

test / 1.25


# In[47]:

new = test / 1.25
new


# In[48]:

new = np.array([2.5, 4.5, 1.5, 3.5])
print new * 0.75
print new
print new * 1.25


# In[ ]:



