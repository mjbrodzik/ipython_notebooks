
# coding: utf-8

# In[1]:

import glob
import matplotlib.pyplot as plt
from netCDF4 import Dataset
import numpy as np
get_ipython().magic(u'pylab inline')


# In[2]:

get_ipython().magic(u'cd ~/projects/PMESDR/CSU_FCDR/F17/1212/121201')
get_ipython().magic(u'ls')


# In[3]:

list = glob.glob("*nc")
list


# In[4]:

f = Dataset(list[0], "r", format="NETCDF")
f


# In[5]:

f.variables['fcdr_tb37h_env2']


# In[33]:

data = f.variables['fcdr_tb37h_env2'][:]
np.shape(data)
f.close()


# In[7]:

np.amin(data), np.amax(data)


# In[9]:

28 * 300


# For 28" wide poster panel at 300 dpi, it should be 8400 pixels across;
# If I keep the 90-pixel wide swaths, this gives me 94 swaths to work with,
# but if i just randomly make them in groups of fibonacci numbers, say:
# 
# 5 + 1 + 2 + 3 + 1 + 2 = 14 + 6 blanks = 20, try this:
# Left side:
# 
# 5 + 1 + 2
# 
# Right side:
# 
# + 3 + 1 + 2 +
# 

# In[76]:

blank = np.zeros((3230,90))
np.shape(blank)


# In[140]:

def add_new_swath(image, image_index, list, list_index):
    f = Dataset(list[list_index], "r", format="NETCDF")
    data = f.variables['fcdr_tb37h_env2'][:]
    image[0:data.shape[0], image_index * 90: (image_index * 90) + data.shape[1]] = data
    print("data:", np.amin(data), np.amax(data))
    print("image:",np.amin(image), np.amax(image))
    f.close()
    return(image)


# In[154]:

my_image = np.zeros((3230,90 * 10))
my_image.fill(250.)
my_image = add_new_swath(my_image, 8, list, 0)
my_image = add_new_swath(my_image, 7, list, 1)
my_image = add_new_swath(my_image, 5, list, 2)
my_image = add_new_swath(my_image, 3, list, 3)
my_image = add_new_swath(my_image, 2, list, 4)
my_image = add_new_swath(my_image, 1, list, 5)


# In[142]:

my_image.shape


# In[155]:

fig, ax = plt.subplots(1, 1)
plt.imshow(my_image, cmap=plt.cm.gray, interpolation='None',
          vmin=50., vmax=300.)
plt.axis('off')


# In[156]:

outfile = "/Users/brodzik/CSU_swath_20121201_right_side.jpg"
fig.savefig(outfile,dpi=1200)


# In[157]:

my_image = np.zeros((3230,90 * 10))
my_image.fill(250.)
my_image = add_new_swath(my_image, 9, list, 6)
my_image = add_new_swath(my_image, 8, list, 7)
my_image = add_new_swath(my_image, 6, list, 8)
my_image = add_new_swath(my_image, 4, list, 9)
my_image = add_new_swath(my_image, 3, list, 10)
my_image = add_new_swath(my_image, 2, list, 11)
my_image = add_new_swath(my_image, 1, list, 12)
my_image = add_new_swath(my_image, 0, list, 13)


# In[160]:

fig, ax = plt.subplots(1, 1)
plt.imshow(my_image, cmap=plt.cm.gray, interpolation='None',
          vmin=50., vmax=300.)
plt.axis('off')


# In[161]:

outfile = "/Users/brodzik/CSU_swath_20121201_left_side.jpg"
fig.savefig(outfile,dpi=1200)


# In[53]:

def swath_shapes(list):
    for filename in list:
        f = Dataset(filename, "r", format="NETCDF")
        print(filename, np.shape(f.variables['fcdr_tb37h_env2']))
        f.close()


# In[54]:

swath_shapes(list)


# In[ ]:



