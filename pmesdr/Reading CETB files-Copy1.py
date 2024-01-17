
# coding: utf-8

# # How to read and examine CETB files
# 
# This notebook shows:
# * how to open, read, examine and display CETB file data
# * how to access EASE-Grid 2.0 projection information and get the map coordinates of the upper left corner
# * how to convert CETB dates from "days since epoch" to Gregorian dates
# * how to use the cetbtools package to do map transformations for lat/lon to/from row/col
# 
# CETB files are available from the globus.org Endpoint "Passive Microwave Prototype ESDR".  Please contact Molly Hardman (molly.hardman_at_nsidc.org) at NSIDC if you have not yet requested an invitation to access the data.
# 
# For this notebook, I have downloaded the first 5 days of 2003 CSU N prototype data to my local directory ~/cetb_data/.  If you wish to run this notebook on your local machine, you may have to adjust the paths in the filenames.
# 
# ## Import required packages for this notebook
# 
# Begin by setting up inline matplotlib display, and importing the netCDF4 reader package:
# 

# In[1]:

get_ipython().magic(u'pylab inline')
import matplotlib.pyplot as plt
from netCDF4 import Dataset, num2date
import numpy as np
import os
from pylab import rcParams
rcParams['figure.figsize'] = 12, 10


# (You may not see this warning about the font cache on your system, apparently it's new behavior from matplotlib on systems with many fonts installed.)
# 
# Next, install and import the cetbtools conda package.  This package contains lat,lon <-> row,col transformation routines for the EASE-Grid 2.0 projections we have used for this project.
# 
# You can install the package on your machine using this command in your local conda env:
# 
# conda install -c https://conda.anaconda.org/nsidc cetbtools
# 
# This package is currently available for python on mac os X and linux platforms.
# 
# Assuming you have cetbtools installed, you should be able to do this:

# In[2]:

from cetbtools.ease2conv import Ease2Transform


# Get help and information about the Ease2Transform class (we will use this class once we have read some data):

# In[3]:

help(Ease2Transform)


# ## Open a CETB file and examine the TB data:
# 
# (You will likely have to change this to the location on your drive where you have downloaded some CETB data):

# In[4]:

get_ipython().magic(u'cd ~/cetb_data')


# In[5]:

get_ipython().magic(u'ls')


# In[6]:

get_ipython().magic(u'cd F13_CSU_N_2003002')


# In[7]:

get_ipython().magic(u'ls')


# Please refer to the ATBD Appendix to understand filenames:
# 
# http://nsidc.org/pmesdr/files/2016/02/MEaSUREs_CETB_ATBD_v0.11.pdf
# 
# Choose a file to open, and display the file-level global attributes:

# In[8]:

filename = "EASE2_N3.125km.F13_SSMI.2003002.37H.E.SIR.CSU.v0.1.nc"
f = Dataset(filename, "r", format="NETCDF4")
f


# Note that this file contains:
# * dimension variables (rows, cols and time) and 
# * data variables (crs, TB, TB_num_samples, Incidence_angle, TB_std_dev and TB_time).  
# 
# ## Get the projection information
# 
# The crs variable contains "coordinate reference system" information about the projection and grid used for this file.  To read the crs variable, use:
# 

# In[9]:

crs = f.variables['crs']
crs


# We have encoded the projection information in several ways in this file, including:
# 
# * CF-compliant projection attributes, including grid_mapping_name and specific attributes origin and false easting/northing for the projection
# * proj4txt: the proj4 string for this projection
# * srid: the EPSG code for this projection
# * crs_wkt: the "well-known text" string that describes the projection
# * long_name: the NSIDC mapx grid paramater definition name
# 
# You can also determine the grid scale factor in meters, from the attribute "scale_factor_at_projection_origin".  
# 
# ## Get the map coordinates of the UL corner
# 
# Finally, if you are looking for the map coordinates (in meters) of the upper left corner of the grid, you can obtain them from the valid_range attributes of the rows and cols dimension variables, like this:
# 

# In[10]:

print f.variables['rows'], f.variables['cols']


# The left edge of cols is (in meters) -9000000. and the top edge of rows is 9000000., so the upper left corner of the upper left cell is [row, col] = [9000000., -9000000.]

# ## Read and display a TB array
# 
# The dimension variables cols and rows indicate that this data is a square array that is 5760 x 5760.  To read the 5760x5760 TB array into memory, use:

# In[11]:

data = f.variables['TB'][:]
print np.shape(data), np.amin(data), np.amax(data)


# We have stored each data array with a single time dimension for the date in order to facilitate netCDF tools that allow data across many files to be concatenated by date.  To work just with the 2D array of data, you can use the numpy "squeeze" function like this:

# In[12]:

data = np.squeeze(data)
print np.shape(data)


# ## Get the date of the data in this file
# 
# You can get the date of the data in this file by examining the time dimension variable:

# In[13]:

d = f.variables['time']
date = d[:]
print d
print date


# Note that this date is encoded as "days since 1972-01-01".  To convert to a Gregorian date, use the num2date function imported from the netCDF4 package, and use the strftime function to format it as various date strings:

# In[14]:

greg_date = num2date(date[:],units=d.units,calendar=d.calendar)
print(greg_date)
print greg_date[0].strftime("%Y-%m-%d")
print greg_date[0].strftime("%b %d %Y")


# ## Display the TB array
# 
# Next, to display the brightness temperatures in this data array as an image, use imshow:

# In[15]:

fig, ax = plt.subplots(1,1)
ax.set_title("%s (%s)" % 
             (os.path.basename(filename), greg_date[0].strftime("%Y-%m-%d")))
plt.imshow(data, cmap=plt.cm.gray, vmin=np.amin(data), vmax=np.amax(data), interpolation='nearest')
plt.axis('off')
plt.colorbar(shrink=0.50,label='TB')


# ## Display the number of measurement samples used for each cell in the image reconstruction
# 
# Similarly, the number of samples used to derive each grid cell in the image reconstruction is in the variable TB_num_samples, which can be read and displayed like this:

# In[16]:

num = np.squeeze(f.variables['TB_num_samples'][:])


# In[17]:

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

# In[18]:

print crs.long_name


# In[19]:

N3grid = Ease2Transform(crs.long_name)


# geographic_to_grid can be used to transform a (lat, lon) coordinate to (row, col).  The returned values for row, col will be real-valued, and need to be rounded (up at 0.5) to get the integer values of row, col that can be used to index into the data arrays:

# In[20]:

(row, col) = N3grid.geographic_to_grid(40., -105.)
print row, col
(irow, icol) = (int(round(row)), int(round(col)))
print irow, icol


# In[21]:

print "TB at (40.0N, 105.0W) is: %f K" % data[irow, icol]
print "Num samples used: %d" % num[irow, icol]


# Use grid_to_geographic to transform a (row, col) coordinate to (lat, lon):

# In[22]:

print N3grid.grid_to_geographic(row,col)


# Lastly, remember to close the netCDF file:

# In[23]:

f.close()


# Feel free to contact us with questions about the data or this tutorial: brodzik_at_nsidc.org.

# In[ ]:



