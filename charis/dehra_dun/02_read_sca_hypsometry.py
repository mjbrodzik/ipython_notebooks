
# coding: utf-8

# # 02_read_sca_hypsometry

# ### <i><p>Purpose of this notebook:  Introduce you to:     <ol>         <li> CHARIS ASCII file format for hypsometry data</li>         <li> pandas (http://pandas.pydata.org), a python module for working with spreadsheet-types of data</li>         <li> my hypsometry.py python module (included in the short course materials) for reading and writing hypsometry data     </ol> </p>     <p>At the end of this lesson, you should be able to read a sample hypsometry file, and:     <ol>         <li> see if it includes comments         <li> figure out how many rows and columns it has         <li> look at the hypsometry data         <li> display one column of data, as a function of time         <li> create and customize figures     </ol> </p></i>

# Let's begin with a few configuration things:
# tell ipython to display plots right here in the notebook, and tell python I want to use numpy (for numerical array types), matplotlib (for making nice plots), and pandas (for working with DataFrames and Series data).
# 
# Configure pandas display options to display big arrays nicely.

# In[1]:

get_ipython().magic(u'pylab inline')
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#pd.describe_option('display')
pd.set_option('display.max_rows', 370)
pd.set_option('display.max_columns', 70)
pd.set_option('display.width', 200)


# CHARIS hypsometry files are ASCII-formatted files that I defined.  I originally worked on them in IDL but python will read and write them also.
# 
# Here's an example file:

# In[2]:

get_ipython().system(u'cat test.sca_by_elev.txt')


# The next cell has an "import" trick that lets you edit a python script, run it, edit the script again and run it again, all from inside ipython:

# In[4]:

from imp import reload
from charistools import hypsometry
filename = "test.sca_by_elev.txt"
sca = hypsometry.Hypsometry()
sca.read( filename, verbose=True )


# In[ ]:

#sca.data.drop?
pd.__version__


# In[ ]:

#%debug


# So this "sca" variable now contains a pandas object that includes two "attributes", a string array with the comments (one comment line each), and a thing called a pandas "DataFrame".
# 
# Pandas DataFrame terminology:
# <ul>
#     <li> rows and columns can be referred to by name as well as integers (like in a matrix)
#     <li> df.index : the names of the rows (hypsometry.py makes these dates)
#     <li> df.columns : the names of the columns (hypsometry.py makes these elevation bands)
# </ul>
#     

# In[ ]:

help( sca )


# In[ ]:

sca.comments


# In[ ]:

sca.data


# Look at the names of rows with the pandas "index" attribute:

# In[ ]:

sca.data.index 
#sca.data.index.tolist()  # equivalently: list( sca.data.index )
#help( sca.data.index)


# In[ ]:

sca.data.index.date


# In[ ]:

list( sca.data.index)


# In[ ]:

sca.write( 'out.txt', verbose=True)
#sca.write( 'out.txt', verbose=True)


# In[ ]:

get_ipython().system(u'cat out.txt')


# In[ ]:

sca.data.describe()


# In[ ]:

sca.data.columns


# In[ ]:

sca.data.ix['2001-01-05','1500.0']


# ## Printing sca for specific dates

# To slice hypsometry data by rows (a range of dates):

# In[ ]:

sca.data.loc['2001-01-01':'2001-01-05']


# To see every 30 days:

# In[ ]:

sca.data.ix[::30]


# To just look at a single column (this will return a pandas "Series" object, basically an index and value for every entry):

# In[ ]:

sca.data['1400.0']


# ## Just look at SCA at selected elevations in this basin:

# In[ ]:

elevations = ['1400.0','2400.0','3400.0','4400.0','5400.0']
sca.data[elevations]


# In[ ]:

sca.data[elevations].plot()


# But notice how the elevations go from highest to lowest, where you'd really want to see lowest to highest:

# In[ ]:

elevations[::-1]


# In[ ]:

sca.data[elevations[::-1]].plot()


# Or you might not want them all on the same plot, maybe separate plots, sharing a y axis range would be better:

# In[ ]:

sca.data[elevations[::-1]].plot( title="Basin SCA at selected elevations",
                                subplots=True, sharey=True, figsize=(12,8) )


# In[ ]:

#help(sca.data)
help(sca)


# ## Total the SCA by date and display basin SCA time series

# I want to do this so often, I wrote a method on the hypsometry Class that will total up each row (date) for all elevations and return a total for each day:

# In[ ]:

sca_by_doy = sca.data_by_doy()
sca_by_doy.head()


# In[ ]:

sca_by_doy.plot( title='Basin SCA, 2001', figsize=(12,8) )


# Here is a diagram showing the three main parts of a figure in matplotlib.pyplot:
# 
# <img src="pyplot_figure_parts.png">
# 
# For more options on matplotlib line styles, see http://matplotlib.org/1.3.1/examples/pylab_examples/line_styles.html

# In[ ]:

fig, ax = plt.subplots(1,1)
ax.set_title('Basin SCA')
ax.set_ylabel('Area (sq km)')
ax.set_ylim([0,15000])
plt.subplots_adjust(bottom=0.15)
# plot style cheatsheet:
# first character specifies color:
#   'b' : blue
#   'g' : green
#   'r' : red
#   'c' : cyan
#   'm' : magenta
#   'y' : yellow
#   'k' : black
# next 1 or 2 characters specify line style:
#   '_' : short horizontal lines
#   '-' : solid line (default)
#   '--' : dashed line
#   ':' : fine dots
#   'o' : solid circles
#   '.' : bigger dots 
sca_by_doy.plot( ax=ax, style='r--', figsize=(12,8) ) # here is another comment


# ## A plot along a row can be plotted as a real hypsometry (with elevations on y-axis and data values on x-axis)

# Just using the default plot function will put the elevation bands on the x-axis, but this isn't very intuitive:

# In[ ]:

sca.data.ix['2001-01-31'].plot()


# So we can turn this around by just asking for a horizontal bar plot:

# In[ ]:

sca.data.ix['2001-01-31'].describe()
sca.data.ix['2001-01-31'].plot( title='Basin SCA by elevation, 2001-01-31', 
                               kind='barh', figsize=(12,8))
#sca.data.ix[['2001-01-31','2001-05-31']].plot( title='Basin SCA by elevation, 2001-01-31', subplots=True, kind='bar', figsize=(12,8))


# In[ ]:

fig, ax = plt.subplots(1,1)
ax.set_title('Basin SCA by elevation, 2001-01-31')
ax.set_xlabel('SCA (sq km)')
ax.set_ylabel('Elevation (m)')
sca.data.ix['2001-01-31'].plot( kind='barh', figsize=(12,12))
ax.set_yticks( ax.get_yticks()[::10] )
ax.set_yticklabels( sca.data.columns[::10] )


# ## All of the built-in matplotlib functions are available, too:

# In[ ]:

fig, ax = plt.subplots(1,1)
ax.set_title('Basin Change in SCA, Jan to Jun')
ax.set_xlabel('January Area (sq km)')
ax.set_ylabel('June Area (sq km)')
#ax.set_aspect('equal')
#ax.set_xlim( [ 0, 600 ] )
#ax.set_ylim( [ 0, 600 ] )
#plt.subplots_adjust(bottom=0.15)

plt.scatter(sca.data.ix['2001-01-31'], sca.data.ix['2001-06-30'] )


# ## Save data to an external file

# In[ ]:

fig.savefig('sca_plot.png', dpi=300 )  # change filename to .pdf to save to different format


# In[ ]:




# In[ ]:



