#!/usr/bin/env python
from configobj import ConfigObj
import numpy as np
import os
import re

class ModelEnv():
    """
    ModelEnv class will keep track of environment configuration for running
    temperature index modelling.

    2015-09-25 M. J. Brodzik brodzik@nsidc.org 303-492-8263
    National Snow & Ice Data Center, Boulder CO
    Copyright (C) 2015 Regents of the University of Colorado at Boulder
    
    """
    tileConfigFile = 'modis_tiles_config.ini'

    def __init__( self, tileConfigFile=None, topDir=None, verbose=False ):
        """
        usage: modelEnv = ModelEnv( tileConfigFile='my_config.ini', verbose=False )

        Initializer for a melt model environment object

        Arguments:

        tileConfigFile: 'modis_tiles_config.ini' in current working directory
          config file to read

        topDir: default is '/projects/CHARIS'
          local value of top-level directory for filename patterns that contain
          wildcard %model_top_dir%
        
        verbose: False
          set to True for verbose output

        """

        if not tileConfigFile is None:
            self.tileConfigFile = tileConfigFile

        try:
            self.tileConfig = ConfigObj( self.tileConfigFile, file_error=True )
        except Exception as e:
            print ( __name__ + ": Error({0})".format( e ) )
            raise

        if not topDir is None:
            self.set_model_top_dir( topDir )

        if verbose:
            print ( __name__ + ": read MODIS tile configuration from " + self.tileConfigFile )

    def set_model_top_dir( self, topDir, verbose=False ):
        """
        usage: modelEnv.set_model_top_dir( '/Users/username', verbose=False )

        Changes the top-level directory for any paths in the config that use
        %MODEL_TOP_DIR% wildcard

        verbose: False
          set to True for verbose output

        Returns True if successful.
        """
        self.tileConfig['model_top_dir'] = topDir

        return( True )
        
    def fixed_filename( self, type=None, drainageID=None, tileID=None, verbose=False ):
        """
        usage: modelEnv.fixed_filename( verbose=False )

        drainageID : drainage name, string of the form ID_basin_at_pourpoint,
                     possible choices:
                     "AM_AmuDarya_at_Chatly"
                     "BR_Bramaputra_at_Bahadurabad"
                     "IN_Hunza_at_Danyour"
                     "IN_Indus_at_Kotri"
                     "IN_UpperIndus_at_Besham"
                     "GA_Ganges_at_Paksey"
                     "SY_SyrDarya_at_TyumenAryk"
        tileID : MODIS tileID to read, string of the form 'hXXvYY', e.g. 'h23v05'
        type : type of data to read, one of: 'basin_mask', 'dem', 'modice'
        verbose: False
                 set to True for verbose output

        basin_mask files require tileID and drainageID
        dem and modice files require tileID

        Returns model input fixed (invariant in time) filename.
        
        """
        if tileID is None:
            raise ValueError( __name__ + ": tileID is required" )
        if type == "basin_mask" and drainageID is None:
            raise ValueError( __name__ + ": drainageID is required for basin_mask data" )
            
        # MODICE data for high Asia is best for 3strikes
        modice_nstrikes = '3'
        
        file = os.path.join( self.tileConfig['input']['fixed'][type]['dir'],
                             self.tileConfig['input']['fixed'][type]['pattern'] )
        p = re.compile( '%MODEL_TOP_DIR%' )
        file = p.sub( self.tileConfig['model_top_dir'], file )
        p = re.compile( '%NSTRIKES%' )
        file = p.sub( modice_nstrikes, file )
        p = re.compile( '%TILEID%' )
        file = p.sub( tileID, file )

        if not drainageID is None:
            p = re.compile( '%DRAINAGEID%' )
            file = p.sub( drainageID, file )

        return( file )
    
    def forcing_filename( self, type=None, tileID=None, yyyy=None, verbose=False ):
        """
        usage: modelEnv.forcing_filename( verbose=False )

        tileID : MODIS tileID to read, string of the form 'hXXvYY', e.g. 'h23v05'
        type : type of data to read, one of: 'modscag_gf'
        verbose: False
                 set to True for verbose output

        modscag_gf files require tileID and yyyy

        Returns model input forcing (time-varying) filename.
        
        """
        if tileID is None:
            raise ValueError( __name__ + ": tileID is required" )
        if yyyy is None:
            raise ValueError( __name__ + ": yyyy is required" )
            
        file = os.path.join( self.tileConfig['input']['forcing'][type]['dir'],
                             self.tileConfig['input']['forcing'][type]['pattern'] )
        p = re.compile( '%MODEL_TOP_DIR%' )
        file = p.sub( self.tileConfig['model_top_dir'], file )
        p = re.compile( '%TILEID%' )
        file = p.sub( tileID, file )
        p = re.compile( '%YYYY%' )
        file = p.sub( str( yyyy ).zfill(4), file )

        return( file )
    
