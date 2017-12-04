
# coding: utf-8

# This notebook will convert plain binary MODICE.v0.4 tile files into CF-compliant .nc files, complete with dimension and projection information.
# 
# The user of these files should be able to make geotiffs with:
# 
# and reproject from the spherical MODICE ellipsoid to wgs84 with:
# 

# In[2]:

from netCDF4 import Dataset
import json


# In[ ]:

# Assume that /projects/CHARIS is sshfs mounted on this machine, and
# that the user has write permission
fid = Dataset('~/projects/CHARIS/snow_cover/modice.v0.4/min05yr_nc/MODICE.v0.4.1test.nc', 'w', format='NETCDF4')
fid.Conventions = "CF-1.6"
fid = Dataset('/home/vagrant/measures-byu/src/prod/cetb_file/templates/cetb_global_template.nc', 'w', format='NETCDF4')
fid.Conventions = "CF-1.6"
fid.title = "MODICE mask for a minimum number of years"
fid.product_version = "v0.4"
#fid.software_version_id = "TBD"
#fid.software_repository = "git@bitbucket.org:nsidc/measures-byu.git"
fid.source = "MODICE"
fid.source_version_id = "v04"
fid.history = ""
fid.comment = "Mask locations with 2 indicate MODICE for >= min_years."
fid.references = "Painter, T. H., Brodzik, M. J., A. Racoviteanu, R. Armstrong. 2012. Automated mapping of Earth's annual minimum exposed snow and ice with MODIS. Geophysical Research Letters, 39(20):L20501, doi:10.1029/2012GL053340."
fid.summary = ["An improved, enhanced-resolution, gridded passive microwave Earth System Data Record \n",
               "for monitoring cryospheric and hydrologic time series\n" ]fid.title = "MEaSUREs Calibrated Passive Microwave Daily EASE-Grid 2.0 Brightness Temperature ESDR"
fid.institution = ["National Snow and Ice Data Center\n",
                   "Cooperative Institute for Research in Environmental Sciences\n",
                   "University of Colorado at Boulder\n",
                   "Boulder, CO"]
fid.publisher = ["National Snow and Ice Data Center\n",
                   "Cooperative Institute for Research in Environmental Sciences\n",
                   "University of Colorado at Boulder\n",
                   "Boulder, CO"]
fid.publisher_url = "http://nsidc.org/charis"
fid.publisher_email = "brodzik@nsidc.org"
fid.project = "CHARIS"
fid.standard_name_vocabulary = "CF Standard Name Table (v27, 28 September 2013)"
fid.cdm_data_type = "grid"
fid.keywords = "EARTH SCIENCE > SPECTRAL/ENGINEERING > MICROWAVE > BRIGHTNESS TEMPERATURE" 
fid.keywords_vocabulary = "NASA Global Change Master Directory (GCMD) Earth Science Keywords, Version 8.1"
fid.platform = "TBD"
fid.sensor = "TBD"
fid.naming_authority = "org.doi.dx"
fid.id = "10.5067/MEASURES/CRYOSPHERE/nsidc-0630.001"
fid.date_created = "TBD"
fid.acknowledgement = ["This data set was created with funding from NASA MEaSUREs Grant #NNX13AI23A.\n",
                       "Data archiving and distribution is supported by the NASA NSIDC Distributed Active Archive Center (DAAC)."]
fid.license = "No constraints on data access or use"
fid.processing_level = "Level 3"
fid.creator_name = "Mary J. Brodzik"
fid.creator_email = "brodzik@nsidc.org"
fid.creator_url = "http://nsidc.org/charis"
fid.contributor_name = "T. H. Painter, M. J. Brodzik, R. L. Armstrong"
fid.contributor_role = "Principal Investigator, Co-Investigator, Co-Investigator"
fid.citation = ["Brodzik, M. J., D. G. Long, M. A. Hardman, A. C. Paget. 2015.\n",
                "MEaSUREs Calibrated Passive Microwave Daily EASE-Grid 2.0 Brightness Temperature ESDR.\n",
                "Version 0.01.\n",
                "[Indicate subset used].\n",
                "Boulder, Colorado USA: NASA DAAC at the National Snow and Ice Data Center." ]

