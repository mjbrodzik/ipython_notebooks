
# coding: utf-8

# In[1]:

get_ipython().magic(u'pylab inline')
import matplotlib.pyplot as plt
from netCDF4 import Dataset, num2date
import numpy as np
import os
from pylab import rcParams
rcParams['figure.figsize'] = 12, 10


# In[2]:

get_ipython().magic(u'cd ~/projects/PMESDR/mahworking/')


# In[3]:

get_ipython().magic(u'ls')


# In[4]:

filename = "CETB37V.2004.3km.d001-d182.nh.nc"
f = Dataset(filename, "r", format="NETCDF4")
f


# In[5]:

data = f.variables['TB'][:3,:,:]
print(data.dtype)
print(data.shape)


# In[6]:

f.close()


# In[7]:

print(np.amin(data),np.amax(data))


# Dump the data as flat binary

# In[8]:

print(type(data))


# In[9]:

cdata = np.ma.filled(data, fill_value=0.0)


# In[10]:

print(type(cdata))


# In[11]:

cdata.tofile(file="/Users/brodzik/cetb_data/CETB37V.2004.3km.d001-d182.nh.TB.0-2.bin")
#help(cdata.tofile)


# In[12]:

get_ipython().magic(u'cd /Users/brodzik/cetb_data')
get_ipython().magic(u'ls -las *.bin')


# In[ ]:

5760 * 5760 * 4


# In[ ]:

data = f.variables['TB'][:]
print np.shape(data), np.amin(data), np.amax(data)


# We have stored each data array with a single time dimension for the date in order to facilitate netCDF tools that allow data across many files to be concatenated by date.  To work just with the 2D array of data, you can use the numpy "squeeze" function like this:

# In[ ]:

data = np.squeeze(data)
print np.shape(data)


# ## Get the date of the data in this file
# 
# You can get the date of the data in this file by examining the time dimension variable:

# In[ ]:

d = f.variables['time']
date = d[:]
print d
print date


# Note that this date is encoded as "days since 1972-01-01".  To convert to a Gregorian date, use the num2date function imported from the netCDF4 package, and use the strftime function to format it as various date strings:

# In[ ]:

greg_date = num2date(date[:],units=d.units,calendar=d.calendar)
print(greg_date)
print greg_date[0].strftime("%Y-%m-%d")
print greg_date[0].strftime("%b %d %Y")


# ## Display the TB array
# 
# Next, to display the brightness temperatures in this data array as an image, use imshow:

# In[ ]:

fig, ax = plt.subplots(1,1)
ax.set_title("%s (%s)" % 
             (os.path.basename(filename), greg_date[0].strftime("%Y-%m-%d")))
plt.imshow(data, cmap=plt.cm.gray, vmin=np.amin(data), vmax=np.amax(data), interpolation='nearest')
plt.axis('off')
plt.colorbar(shrink=0.50,label='TB')


# ## Display the number of measurement samples used for each cell in the image reconstruction
# 
# Similarly, the number of samples used to derive each grid cell in the image reconstruction is in the variable TB_num_samples, which can be read and displayed like this:

# In[ ]:

num = np.squeeze(f.variables['TB_num_samples'][:])


# In[ ]:

fig, ax = plt.subplots(1,1)
ax.set_title("%s (%s)" % 
             (os.path.basename(filename), greg_date[0].strftime("%Y-%m-%d")))
plt.imshow(num, cmap=plt.cm.gray, vmin=np.amin(num), vmax=np.amax(num), interpolation='nearest')
plt.axis('off')
plt.colorbar(shrink=0.50,label='Num')


# ## Doing (row,col) <--> (lat, lon) map transformations
# 
# To get the TB temperature at a specific geolocation, use the Ease2Transform class.  The initializer for this class need only be called once, and then the "geographic_to_grid" or "grid_to_geographic" methods can be called repeatedly.  The initializer takes one input argument, the NSIDC mapx name for the projection and grid that is stored in the crs.long_name attribute we examined earlier:
# 

# In[ ]:

print crs.long_name


# In[ ]:

N3grid = Ease2Transform(crs.long_name)


# geographic_to_grid can be used to transform a (lat, lon) coordinate to (row, col).  The returned values for row, col will be real-valued, and need to be rounded (up at 0.5) to get the integer values of row, col that can be used to index into the data arrays:

# In[ ]:

(row, col) = N3grid.geographic_to_grid(40., -105.)
print row, col
(irow, icol) = (int(round(row)), int(round(col)))
print irow, icol


# In[ ]:

print "TB at (40.0N, 105.0W) is: %f K" % data[irow, icol]
print "Num samples used: %d" % num[irow, icol]


# Use grid_to_geographic to transform a (row, col) coordinate to (lat, lon):

# In[ ]:

print N3grid.grid_to_geographic(row,col)


# Original header files for EASE-Grid (721x721) from Terry tied
# x,y = (1.5, 1.5) to the coordinate in meters for (0.0, 0.0)
# I think this is due to some convention in ENVI that Terry indentified a long time ago.
# So, for original Nl.gpd:

# In[ ]:

ease_scale_km = 200.5402 / 8.
ease_scale_km


# In[ ]:

print(ease_scale_km * 1000. * 360.)


# Terry says for EASE-Grid 2.0 .hdrs, set the coordinates at 1.0, 1.0 to the UL corner cell, so we can use the same
# coordinate for any of the nested versions

# In[ ]:

ease2_scale_km = 25.0


# In[ ]:

print(ease2_scale_km * 1000. * 360.0)


# In[ ]:

get_ipython().magic(u'pwd')


# In[ ]:

25000. / 8.


# In[13]:

2667.*2098*364*2


# In[ ]:



