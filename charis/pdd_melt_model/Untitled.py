
# coding: utf-8

# In[1]:

from configobj import ConfigObj


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


# In[37]:

config = ConfigObj('modis_tiles_config.ini')
print config['modis_tile']['rows']
print config['input']['fixed']['basin_mask']['dir']
print config['input']['fixed']['basin_mask']['pattern']
print config['input']['fixed']['basin_mask']['type']
print config['input']['fixed']['country_mask']['pattern']


# In[34]:

print config.initial_comment


# In[36]:

print config['input'].comments


# In[ ]:




# In[ ]:



