
# coding: utf-8

# In[1]:

get_ipython().magic(u'pylab inline')
import matplotlib.pyplot as plt
import numpy as np

from charistools.readers import read_tile
pylab.rcParams['figure.figsize'] = (10.0, 8.0)


# In[2]:

get_ipython().magic(u'cd /Users/brodzik/projects/CHARIS_FTP_copy/main_training/data/basin_masks')
get_ipython().magic(u'ls')


# In[3]:

h23= read_tile('IN_Hunza_at_Danyour.basin_mask.h23v05.tif')
h24= read_tile('IN_Hunza_at_Danyour.basin_mask.h24v05.tif')


# In[4]:

np.amin(h23), np.amax(h23)


# In[9]:

fig, ax = plt.subplots(1,1)
plt.imshow(h24)


# In[16]:

left = h23[h23==1]
print(left.shape)
right = h24[h24==1]
print(right.shape)


# In[15]:

kmperpixel = 463.312717 * 463.312717 / (1E6)
print(kmperpixel)


# In[17]:

print((22796.+41081.)*kmperpixel)


# In[ ]:

print np.amin(diff)
print np.amax(diff)


# In[ ]:

print(data[1:2,:])


# In[ ]:

test = np.array([3.2, 5.6, 2.0, 4.4])
test


# In[ ]:

test / 1.25


# In[ ]:

new = test / 1.25
new


# In[ ]:

new = np.array([2.5, 4.5, 1.5, 3.5])
print new * 0.75
print new
print new * 1.25


# In[ ]:



