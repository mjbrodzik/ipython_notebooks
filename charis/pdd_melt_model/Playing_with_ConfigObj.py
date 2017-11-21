
# coding: utf-8

# In[4]:

from configobj import ConfigObj


# In[7]:

config = ConfigObj('odis_tiles_config.ini')
print config
print type(config)


# In[8]:

get_ipython().set_next_input(u'config = ConfigObj');get_ipython().magic(u'pinfo ConfigObj')


# In[ ]:

config = ConfigObj


# In[13]:

config = ConfigObj()
config.indent_type = '    '
config.initial_comment = [
    "Configuration file for CHARIS melt modeling",
]
input_section = {
    'forcing': {
        'temperature': {
            'path': '/path/to/temperature/data',
            'pattern': 'filename%pattern%',
            'type': 'type_of_file(binary, etc)'
        }
    }
}
config['input'] = input_section
config['output'] = {}
config['validation'] = {}
config.filename = 'test_config.ini'
config.write()



# In[21]:

get_ipython().system(u'ls')


# In[3]:

config = ConfigObj('modis_tiles_config.ini')
print config['modis_tile']['rows']
print config['input']['fixed']['basin_mask']['dir']
print config['input']['fixed']['basin_mask']['pattern']
print config['input']['fixed']['basin_mask']['type']
print config['input']['fixed']['country_mask']['pattern']


# In[3]:

print config.initial_comment


# In[36]:

print config['input'].comments


# In[ ]:




# In[ ]:



