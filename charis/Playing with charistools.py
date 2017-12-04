
# coding: utf-8

# In[19]:

from charistools import hypsometry, modis_info
from netCDF4 import Dataset
import numpy as np
from osgeo import gdal
import matplotlib.pyplot as plt


# In[2]:

modis_info.area_per_500m_pixel_km2


# In[3]:

help(hypsometry)


# In[7]:

hyps = hypsometry.Hypsometry(comments=['some comments'])


# In[9]:

hyps.comments


# In[10]:

hyps.data


# In[11]:

get_ipython().magic(u'cd /Users/brodzik/projects/CHARIS/snow_cover/modice.v0.4/min05yr_nc')
get_ipython().magic(u'ls')


# In[13]:

file = Dataset('MODICE.v0.4.h23v05.1strike.min05yr.mask.nc', mode='r', format='NETCDF4')


# In[14]:

file


# In[15]:

modice = file.variables["modice_min_year_mask"][:]


# In[17]:

np.shape(modice)


# In[20]:

get_ipython().magic(u'cd /Users/brodzik/projects/CHARIS/elevation_data/SRTMGL3')
get_ipython().magic(u'ls')


# In[22]:

elevation_file = 'SRTMGL3.v0.1.h23v05.tif'
dataset = gdal.Open(elevation_file, gdal.GA_ReadOnly)


# In[24]:

dataset.RasterCount


# In[25]:

band = dataset.GetRasterBand(1)
elevation = band.ReadAsArray()


# In[26]:

np.shape(elevation)


# In[27]:

np.amin(elevation)


# In[28]:

np.amax(elevation)


# In[29]:

hyps


# In[30]:

hyps.comments


# In[31]:

hyps.append(elevation,modice,min_contour_m=1400,verbose=True)


# In[32]:

hyps.data


# In[33]:

hypsh23v05 = hyps


# In[35]:

elevation_file_h24 = 'SRTMGL3.v0.1.h24v05.tif'
dataset24 = gdal.Open(elevation_file_h24, gdal.GA_ReadOnly)
band24 = dataset24.GetRasterBand(1)
elevation24 = band24.ReadAsArray()


# In[36]:

np.amin(elevation24)


# In[37]:

np.amax(elevation24)


# In[38]:

get_ipython().magic(u'cd /Users/brodzik/projects/CHARIS/snow_cover/modice.v0.4/min05yr_nc')
get_ipython().magic(u'ls')


# In[39]:

file24 = Dataset('MODICE.v0.4.h24v05.1strike.min05yr.mask.nc', mode='r', format='NETCDF4')


# In[40]:

modice24 = file24.variables["modice_min_year_mask"][:]


# In[41]:

print(np.amin(modice24),np.amax(modice24))


# In[42]:

hypsh24v05 = hypsometry.Hypsometry(comments=['h24v05'])


# In[43]:

hypsh24v05.append(elevation24,modice24,min_contour_m=1400,verbose=True)


# In[44]:

hypsh23v05.data


# In[45]:

hypsh24v05.data


# In[46]:

all = hypsh23v05.data + hypsh24v05.data


# In[47]:

all


# In[50]:

orig = hypsometry.Hypsometry(filename='/Users/brodzik/projects/CHARIS/snow_cover/modice.v0.4/IN_Hunza_at_Danyour.0100m.modicev04_1strike_area_by_elev.txt')


# In[51]:

orig.data


# In[ ]:



