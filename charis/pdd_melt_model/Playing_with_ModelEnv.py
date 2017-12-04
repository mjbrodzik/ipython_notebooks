
# coding: utf-8

# In[1]:

from imp import reload
import modelEnv
reload(modelEnv)
myEnv = modelEnv.ModelEnv( topDir='/Users/brodzik/projects/CHARIS/charis_training_2015_data', verbose=True )
print myEnv.fixed_filename( type='modice', tileID='h23v05', verbose=True )


# In[2]:

from netCDF4 import Dataset
modice_filename = myEnv.fixed_filename( type='modice', tileID='h23v05', verbose=True )
fid = Dataset(modice_filename, 'r', format='NETCDF4')
fid


# In[3]:

modice = fid.variables['modice_min_year_mask']
modice


# In[4]:

data = modice[:]
data.shape


# In[5]:

type(data)


# In[6]:

import numpy as np
print np.amin(data), np.amax(data)


# In[8]:

import matplotlib.pyplot as plt
plt.imshow( data, cmap='gray' )
plt.show()


# In[ ]:



