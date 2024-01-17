
# coding: utf-8

# In[3]:

import cetbtools.inspector as ci


# In[9]:

get_ipython().magic(u'cd /Users/brodzik/cetb_data/AQUA')


# In[10]:

get_ipython().magic(u'ls')


# In[4]:

help(ci)


# In[12]:

ci.make_cetb_geotiff(cetb_filename="EASE2_T3.125km.AQUA_AMSRE.2003004.36H.A.SIR.RSS.v0.1.nc", verbose=True)


# In[13]:

get_ipython().magic(u'ls')


# Joan's Himalayan region: 27N, 105E to 46N, 62E

# In[15]:

lat, lon = 27., 105.
(row, col) = T25grid.geographic_to_grid(lat, lon)
(x, y) = T25grid.grid_to_map(row, col)
print "lat/lon=", lat, lon
print "row/col=", row, col
print "x/y =   ", x, y


# In[16]:

lat, lon = 46., 62.
(row, col) = T25grid.geographic_to_grid(lat, lon)
(x, y) = T25grid.grid_to_map(row, col)
print "lat/lon=", lat, lon
print "row/col=", row, col
print "x/y =   ", x, y



# Russian High Arctic: 82N, 45E to 70N, 110E

# In[17]:

lat, lon = 82., 45.
(row, col) = N25grid.geographic_to_grid(lat, lon)
(x, y) = N25grid.grid_to_map(row, col)
print "lat/lon=", lat, lon
print "row/col=", row, col
print "x/y =   ", x, y
lat, lon = 70., 110.
(row, col) = N25grid.geographic_to_grid(lat, lon)
(x, y) = N25grid.grid_to_map(row, col)
print "lat/lon=", lat, lon
print "row/col=", row, col
print "x/y =   ", x, y


# Alaska and Yukon River: 73N, 170W to 55N, 125W

# In[18]:

lat, lon = 73., -170.
(row, col) = N25grid.geographic_to_grid(lat, lon)
(x, y) = N25grid.grid_to_map(row, col)
print "lat/lon=", lat, lon
print "row/col=", row, col
print "x/y =   ", x, y
lat, lon = 55., -125.
(row, col) = N25grid.geographic_to_grid(lat, lon)
(x, y) = N25grid.grid_to_map(row, col)
print "lat/lon=", lat, lon
print "row/col=", row, col
print "x/y =   ", x, y


# In[ ]:



