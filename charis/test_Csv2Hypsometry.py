
# coding: utf-8

# In[1]:

from charistools.convertors import Csv2Hypsometry


# In[2]:

get_ipython().magic(u'cd /Users/brodzik/charistools/source/charistools/test')


# In[3]:

get_ipython().magic(u'ls')


# In[4]:

help(Csv2Hypsometry)


# In[5]:

get_ipython().magic(u'cat Kta_hypso_100m.csv')


# In[6]:

csv_filename = "Kta_hypso_100m.csv"
out_filename = "Kta_hypso_100m.txt"
comments = ["Some test comments here about how Kta_Hypso was created."]


# In[7]:

Csv2Hypsometry(csv_filename, out_filename,comments, verbose=True)


# In[8]:

get_ipython().magic(u'cat Kta_hypso_100m.txt')


# In[ ]:



