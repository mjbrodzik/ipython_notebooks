
# coding: utf-8

# <h2>Display hypsometry data</h2>

# In[2]:

get_ipython().magic(u'matplotlib notebook')

from charistools.modelEnv import ModelEnv
from charistools.hypsometry import Hypsometry
import matplotlib.pyplot as plt
#pylab.rcParams['figure.figsize'] = (16.0, 8.0)


# In[3]:

tileConfigFile = '/Users/brodzik/charis_training_2015/' + 'module05_temperature_index_model/modis_tiles_config.ini'
topDir = '/Users/brodzik/projects/CHARIS'
myEnv = ModelEnv(topDir=topDir, tileConfigFile=tileConfigFile, verbose=True)


# In[12]:

import os
os.getcwd()


# In[3]:

station_tempFile = '/Users/brodzik/projects/CHARIS/forcing_data/Observed/air_temperature/derived/' + 'v1.0/hunza_observation_tavg_profile_100m.2001.dscale.v1.0.asc'
drainageID = "IN_Hunza_GDBD"
year = 2001
uncorrected_tempFile = myEnv.hypsometry_filename(drainageID=drainageID, type='temperature_by_elevation', year=year)
corrected_tempFile = '/Users/brodzik/projects/CHARIS/forcing_data/Downscaled/ERA-Interim/day/' + 'corrected/by_elevation/IN_Hunza_GDBD.2001.0100m.corrected.v2.temperature_by_elev.txt'
print station_tempFile
print uncorrected_tempFile
print corrected_tempFile


# In[4]:

station_temp_hyps = Hypsometry(filename=station_tempFile)
uncorrected_temp_hyps = Hypsometry(filename=uncorrected_tempFile)
corrected_temp_hyps = Hypsometry(filename=corrected_tempFile)


# In[ ]:

#%ls /Users/brodzik/projects/CHARIS/forcing_data/Downscaled/ERA-Interim/day/corrected/by_elevation


# In[5]:

print(station_temp_hyps.data.columns)
print(uncorrected_temp_hyps.data.columns)
print(corrected_temp_hyps.data.columns)


# <h2>Adjust station temps from Kelvin to degrees-C</h2>

# In[6]:

station_temp_hyps.data = station_temp_hyps.data - 273.15
station_temp_hyps.data.describe()


# In[7]:

corrected_temp_hyps.data.describe()


# In[8]:

uncorrected_temp_hyps.data.describe()


# In[9]:

station_temp_by_doy = (station_temp_hyps.data_by_doy() / len(station_temp_hyps.data.columns))
corrected_temp_by_doy = corrected_temp_hyps.data_by_doy() / len(corrected_temp_hyps.data.columns)
uncorrected_temp_by_doy = uncorrected_temp_hyps.data_by_doy() / len(uncorrected_temp_hyps.data.columns)


# In[10]:

fig, ax = plt.subplots()
station_temp_by_doy.plot(color='k', linestyle='--',                          title=drainageID + " avg basin temperatures " + str(year), label='Stations')
corrected_temp_by_doy.plot(color='r', linestyle=':', label='Downscaled, Corrected')
uncorrected_temp_by_doy.plot(color='k', linestyle=':', label='Downscaled, Uncorrected')
ax.set_ylabel('Temperature')
legend = ax.legend()
fig.savefig("/Users/brodzik/charis/IN_Hunza_observed_vs_corrected_downscaled_temps.png")


# In[ ]:

len(old_temp_hyps.data[str(3000 + 50)])



# <h3> Look at a few sample elevations</h3>
# 

# In[ ]:

elevations = [2000, 3000, 4000, 5000, 6000, 7000]
print old_temp_hyps.data
print temp_hyps.data
#print len(old_temp_hyps.data[str(elevations + 50)])
#print len(temp_hyps.data[str(float(elevations))][:-1])


# In[ ]:

elevations = [2000, 3000, 4000, 5000, 6000, 7000]
nrows = 2
ncols = 3
fig, ax = plt.subplots(nrows, ncols)

fig.suptitle('IN_Hunza station vs. downscaled temperatures 2001', fontsize=18)
for i, el in enumerate(elevations):
    row = i / ncols
    col = i % ncols
    this_ax = ax[row, col]
    this_ax.scatter(old_temp_hyps.data[str(el + 50)], temp_hyps.data[str(float(el))])
    lims = [
        np.min([this_ax.get_xlim(), this_ax.get_ylim()]),  # min of both axes
        np.max([this_ax.get_xlim(), this_ax.get_ylim()]),  # max of both axes
    ]

    # now plot both limits against eachother
    this_ax.plot(lims, lims, 'k-')
    # this_ax.plot(lims, lims, 'k-', alpha=0.75, zorder=0)
    this_ax.set_aspect('equal')
    this_ax.set_xlim(lims)
    this_ax.set_ylim(lims)
    this_ax.set_xlabel('Stations')
    this_ax.set_ylabel('Downscaled')
    this_ax.set_title(str(el))
    
fig.tight_layout()
fig.savefig("IN_Hunza_observed_vs_downscaled_temps.scatter.png")


# In[ ]:

station_temp_hyps.data.plot.box(vert=False,positions=np.arange(len(station_temp_hyps.data.columns)),
                                grid=True, title='Stations', label='stations')
uncorrected_temp_hyps.data.plot.box(vert=False,                                     grid=True, title='Uncorrected dscale',                                     color='k',                                     positions=np.arange(len(uncorrected_temp_hyps.data.columns)),label='uncorrected_dscale')
corrected_temp_hyps.data.plot.box(vert=False,                                   grid=True, title='Corrected dscale',                                   color='r',                                   positions=np.arange(len(corrected_temp_hyps.data.columns)),label='corrected_dscale')

#for i, el in enumerate(station_temp_hyps.data.columns):
#    if i < 2:
#        x = station_temp_hyps.data[el].values
#        y.fill(int(el))
#        ax.plot()


# In[11]:

clim=(-10,10)
fig, ax = plt.subplots(1,5, figsize=(16,8))
ax[0].imshow(station_temp_hyps.data.values, cmap='RdBu_r', aspect='auto', clim=clim)
ax[0].set_title('Stations')
ax[1].imshow(corrected_temp_hyps.data.values, cmap='RdBu_r', aspect='auto', clim=clim)
ax[1].set_title('Dscale corrected')
ax[2].imshow(corrected_temp_hyps.data.values - station_temp_hyps.data.values, cmap='RdBu_r', aspect='auto', clim=clim)
ax[2].set_title('corrected-sta')
ax[3].imshow(uncorrected_temp_hyps.data.values, cmap='RdBu_r', aspect='auto', clim=clim)
ax[3].set_title('Dscale uncorrected')
ax[4].imshow(uncorrected_temp_hyps.data.values - station_temp_hyps.data.values, cmap='RdBu_r', aspect='auto', clim=clim)
ax[4].set_title('uncorrected-sta')


# <h2>Read the 3-surface partition files for this year</h2>

# In[15]:

get_ipython().magic(u'cat /Users/brodzik/charis_training_2015/iPython_notebooks/temp_index_model/modis_tiles_config.ini')


# In[25]:

EGIFile = myEnv.hypsometry_filename(drainageID=drainageID, type='exposed_glacier_ice_by_elevation',year=2001,threshold=205)
EGIFile


# In[19]:

SOLFile = myEnv.hypsometry_filename(drainageID=drainageID, type='snow_on_land_by_elevation', year=2001)
SOLFile


# In[21]:

SOIFile = myEnv.hypsometry_filename(drainageID=drainageID, type='snow_on_ice_by_elevation', year=2001,threshold=205)
SOIFile


# In[26]:

egi_hyps = Hypsometry(filename=EGIFile)
sol_hyps = Hypsometry(filename=SOLFile)
soi_hyps = Hypsometry(filename=SOIFile)


# In[27]:

egi_hyps.data


# In[28]:

sol_hyps.data


# In[29]:

soi_hyps.data


# In[ ]:



