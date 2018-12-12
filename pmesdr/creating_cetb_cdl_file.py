
# coding: utf-8

# In[1]:

from netCDF4 import Dataset


# In[10]:

fid = Dataset('cetb_global_template.nc', 'w', format='NETCDF4')
fid.Conventions = "CF-1.6"
fid.title = "MEaSUREs Calibrated Passive Microwave Daily EASE-Grid 2.0 Brightness Temperature ESDR"
fid.product_version = "v00.01"
fid.software_version = "TBD"
fid.software_repository = "git@bitbucket.org:nsidc/measures-byu.git"
fid.source = "TBD"
fid.history = "TBD(bgi or sir)"
fid.comment = "Prototype version of this product, intended for user evaluation and feedback."
fid.references = ["Data set documentation: http://nsidc.org/data/nsidc-0630.html\n",
                  "Algorithm Theoretical Basis Document: http://nsidc.org/pmesdr/files/2015/09/MEaSUREs_CETB_ATBD_v0.10.pdf\n",
                  "Ancillary File: TBD"]
fid.summary = ["An improved, enhanced-resolution, gridded passive microwave Earth System Data Record \n",
               "for monitoring cryospheric and hydrologic time series\n" ]
fid.institution = ["National Snow and Ice Data Center\n",
                   "Cooperative Institute for Research in Environmental Sciences\n",
                   "University of Colorado at Boulder\n",
                   "Boulder, CO"]
fid.publisher = ["National Snow and Ice Data Center\n",
                   "Cooperative Institute for Research in Environmental Sciences\n",
                   "University of Colorado at Boulder\n",
                   "Boulder, CO"]
fid.publisher_url = "http://nsidc.org"
fid.publisher_email = "nsidc@nsidc.org"
fid.project = "NASA 2012 MEaSUREs (Making Earth System Data Records for Use in Research Environments)"
fid.standard_name_vocabulary = "CF Standard Name Table (v27, 28 September 2013)"
fid.cdm_data_type = "grid"
fid.keywords = "EARTH SCIENCE > SPECTRAL/ENGINEERING > MICROWAVE > BRIGHTNESS TEMPERATURE" 
fid.keywords_vocabulary = "NASA Global Change Master Directory (GCMD) Earth Science Keywords, Version 6.0"
fid.platform = "TBD"
fid.sensor = "TBD"
fid.naming_authority = "org.doi.dx"
fid.id = "10.5067/MEASURES/CRYOSPHERE/nsidc-0630.001"
fid.date_created = "TBD"
fid.acknowledgement = ["This data set was created with funding from NASA MEaSUREs Grant #NNX13AI23A.\n",
                       "Data archiving and distribution is supported by NASA Grant #(DAAC Grant ID)."]
fid.license = "TBD"
fid.processing_level = "Level 3"
fid.creator_name = "Mary J. Brodzik"
fid.creator_email = "brodzik@nsidc.org"
fid.creator_url = "http://nsidc.org/pmesdr"
fid.contributor_name = "Mary J. Brodzik"
fid.contributor_role = "Principal Investigator"
fid.contributor_name = "David G. Long"
fid.contributor_role = "Co-Investigator"
fid.contributor_name = "Molly A. Hardman"
fid.contributor_role = "Developer"
fid.contributor_name = "Aaron C. Paget"
fid.contributor_role = "Contributor"
fid.citation = ["Brodzik, M. J., D. G. Long, M. A. Hardman, A. C. Paget. 2015.\n",
                "MEaSUREs Calibrated Passive Microwave Daily EASE-Grid 2.0 Brightness Temperature ESDR.\n",
                "Version 00.01.\n",
                "[Indicate subset used].\n",
                "Boulder, Colorado USA: NASA DAAC at the National Snow and Ice Data Center." ]
fid.close()


# In[7]:

get_ipython().magic(u'ls')


# In[5]:

get_ipython().magic(u'/usr/local/bin/ncdump cetb_N_template.nc')


# In[ ]:



