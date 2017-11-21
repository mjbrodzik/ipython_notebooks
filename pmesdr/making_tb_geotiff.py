
# coding: utf-8

# In[3]:

get_ipython().magic(u'pylab inline')
from cetbtools.inspector import make_cetb_geotiff
import matplotlib.pyplot as plt
import os
import glob


# In[4]:

get_ipython().magic(u'cd ~/cetb_data')


# In[5]:

list = glob.glob("F13*S_2003182/EASE2_*3.125*85H.E.SIR.CSU*nc")
list


# In[6]:

for file in list:
    make_cetb_geotiff(cetb_filename=file, verbose=True)


# In[ ]:

grid = 'e2t_25'
#file = '/projects/PMESDR/vagrant/brodzik/' + grid + '/FD4a-E2T97-061-061.lis_dump.nc'
#file = '/projects/PMESDR/vagrant/brodzik/' + grid + '/FD4m-E2N97-061-061.lis_dump.nc'
file = '/projects/PMESDR/vagrant/brodzik/bgiRSS/' + grid + '/FD4a-E2T97-061-061.lis_dump1.nc'
f = Dataset( file, 'r', 'NETCDF4' )


# In[ ]:

# This should not be necessary, if the data are in the netCDF file properly
# Needs some investigation, could be FORTRAN-C-netCDF nonsense
tb = f.variables[ 'bgi_image' ][ : ]
cols, rows = shape( tb )
print cols, rows
tb = tb.reshape( rows, cols )


# In[ ]:

fig, ax = plt.subplots(1,1)
figsize(12,10)
ax.set_title( os.path.basename( file ) + ' (' + grid + ')' )
# Flip the image to display properly in python
plt.imshow(np.flipud(tb), cmap=plt.cm.gray, vmin=100, vmax=320 )
plt.axis('off')
plt.colorbar( shrink=0.35, label='TB' )
#plt.colorbar( shrink=0.95, label='TB' )


# In[ ]:

outfile = file + '.tif'
driver = gdal.GetDriverByName("GTiff")


# In[ ]:

dst_ds = driver.Create(outfile, cols, rows, 1, gdal.GDT_UInt16)


# In[ ]:

proj = osr.SpatialReference()
# ease2_t:
# when we can connect to epsg v8.6, we should be able to do this: proj.SetWellKnownGeogCS("EPSG:6933")
proj.SetFromUserInput("+proj=cea +lat_0=0 +lon_0=0 +lat_ts=30 +x_0=0 +y_0=0 +ellps=WGS84 +datum=WGS84 +units=m")
# E2N
#proj.SetFromUserInput("+proj=laea +lat_0=90 +lon_0=0 +x_0=0 +y_0=0 +ellps=WGS84 +datum=WGS84 +units=m")
# E2S
#proj.SetFromUserInput("+proj=laea +lat_0=-90 +lon_0=0 +x_0=0 +y_0=0 +ellps=WGS84 +datum=WGS84 +units=m")
dst_ds.SetProjection(proj.ExportToWkt())


# In[ ]:

print proj.ExportToPrettyWkt()


# In[ ]:

# Thanks to web page at:
# http://geoexamples.blogspot.com/2012/01/creating-files-in-ogr-and-gdal-with.html
# The geotransform defines the relation between the raster coordinates x, y and the 
# geographic coordinates, using the following definition:
# Xgeo = geotransform[0] + Xpixel*geotransform[1] + Yline*geotransform[2]
# Ygeo = geotransform[3] + Xpixel*geotransform[4] + Yline*geotransform[5]
# The first and fourth parameters define the origin of the upper left pixel 
# The second and sixth parameters define the pixels size. 
# The third and fifth parameters define the rotation of the raster.
# These values are for EASE2_T25km only, values are meters
#E2T_25
scale = 25025.26000
#E2T_3
#scale = 3128.15750
#E2N_25 or E2S_25
#scale = 25000.00000
#E2N_3 or E2S_3
#scale = 3125.00000
# E2T
map_UL_x = -17367530.44
map_UL_y = -6756820.20000
# E2N or E2S
#map_UL_x = -9000000.
#map_UL_y = -9000000.
geotransform = (map_UL_x,scale,0.,map_UL_y,0.,scale)
dst_ds.SetGeoTransform(geotransform)


# In[ ]:

# Convert tb array to UInt16
print tb.dtype
new = (tb + 0.5).astype(uint16)


# In[ ]:

dst_ds.GetRasterBand(1).WriteArray(new)


# In[ ]:

dst_ds = None


# In[ ]:

print outfile


# In[ ]:

print "Hello world"



# In[ ]:




# In[ ]:



