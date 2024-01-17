
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
get_ipython().magic(u'pylab inline')


# In[26]:

get_ipython().magic(u'cd /Users/brodzik/charis')
get_ipython().magic(u'ls')
filename = 'Hunza_calibration_batch_model.stats.2016-19-Apr.0-80.txt'
#filename = 'Hunza_calibration_batch_model.stats.2016-Apr.all.txt'


# In[27]:

df = pd.read_table(filename, sep='\s+')
subdf = df[['Model_Config','Monthly_Vol_Diff_pcent','Monthly_RMSE']]
subdf


# In[28]:

for name, group in subdf.groupby(['Model_Config']):
    print(name)
    print(group)


# In[29]:

mean_vol_diff = subdf.groupby(['Model_Config']).mean()['Monthly_Vol_Diff_pcent']
mean_rmse = subdf.groupby(['Model_Config']).mean()['Monthly_RMSE']


# In[30]:

new = mean_rmse.to_frame()
new['Monthly_Vol_Diff_pcent'] = mean_vol_diff
new


# In[31]:

min_vol_diff = np.min(mean_vol_diff)
max_vol_diff = np.max(mean_vol_diff)
print("min vol_diff=%f" % min_vol_diff)
print("max_vol_diff=%f" % max_vol_diff)


# In[32]:

min_rmse = np.min(mean_rmse)
max_rmse = np.max(mean_rmse)
print("min rmse=%f" % min_rmse)
print("max rmse=%f" % max_rmse)


# <h2>Now, normalize the two variables so they range from 0.0 to 1.0</h2>
# This should map vol_diff -224.9 to 0. and -110.8 to 1.0
# 
# and             rmse 1.22 to 0. and 2.42 to 1.0:
# 

# In[33]:

new['z_Vol_Diff'] = (new['Monthly_Vol_Diff_pcent'] - min_vol_diff) / (max_vol_diff - min_vol_diff)
new['z_RMSE'] = (new['Monthly_RMSE'] - min_rmse) / (max_rmse - min_rmse)
new['z'] = new['z_Vol_Diff'] + new['z_RMSE']
new


# Now calculate the combined statistic (z_vol_diff + z_rmse) and find the minimum:
# 

# In[34]:

new['z'].plot(kind='barh',figsize=(12,20))


# In[35]:

sorted = new.sort(['z'], ascending=True)
sorted


# In[36]:

print("Best model is %s" % sorted.index[0])


# In[ ]:




# In[ ]:



