
# coding: utf-8

# In[1]:

get_ipython().magic(u'pylab inline')


# In[5]:

from charistools.hypsometry import Hypsometry as hyps
from charistools.convertors import Csv2Hypsometry
import matplotlib.pyplot as plt
import numpy as np
# from scipy import stats


# In[6]:

help(Csv2Hypsometry)


# In[11]:

filename = "/Users/brodzik/projects/CHARIS/pdd_melt_model/2015_paper/Hunza_calibration/best_model/" +         "IN_Hunza_at_Danyour.2004.0100m.GRSIZE_SCAG.0215.ice_melt.dat"
new = hyps(filename=filename, verbose=True)
new


# In[12]:

new.data


# In[19]:

#new.data['5000.']
stats.describe(new.data['5000.'])


# In[24]:

plt.plot(new.data['5000.'])


# In[25]:

from charistools.modelEnv import ModelEnv


# In[26]:

myEnv=ModelEnv()


# In[29]:

strikes=2
strikes


# In[28]:

str(strikes)


# In[ ]:

test

