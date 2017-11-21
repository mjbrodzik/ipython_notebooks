'''
Nose tests for modelEnv

To run tests : nosetests    test_modelEnv.py
Verbose (-v) : nosetests -v test_modelEnv.py

2015-09-25 M. J. Brodzik 303-492-8263 brodzik@nsidc.org
National Snow & Ice Data Center, University of Colorado at Boulder
Copyright (c) 2015 Regents of the University of Colorado

'''
from nose.tools import assert_equals
from nose.tools import assert_raises
import modelEnv

verbose = False
topDir = '/Users/brodzik/projects/CHARIS/charis_training_2015_data'

def test_init_modelEnv_bogus_file():
    assert_raises( IOError, modelEnv.ModelEnv, tileConfigFile='bogus.ini' )

def test_init_modelEnv_with_topDir():
    myEnv = modelEnv.ModelEnv( topDir='/test' )
    assert_equals( myEnv.tileConfig['model_top_dir'],
                   "/test" )

def test_set_model_top_dir():
    myEnv = modelEnv.ModelEnv()
    assert_equals( myEnv.tileConfig['model_top_dir'],
                   "/projects/CHARIS" )
    assert_equals( myEnv.set_model_top_dir( topDir=topDir ), True )
    assert_equals( myEnv.tileConfig['model_top_dir'],
                   topDir )

def test_modice_filename_no_tileID():
    myEnv = modelEnv.ModelEnv( topDir=topDir )
    assert_raises( ValueError, myEnv.fixed_filename )

def test_basin_filename_no_drainageID():
    myEnv = modelEnv.ModelEnv( topDir=topDir )
    assert_raises( ValueError, myEnv.fixed_filename, type='basin_mask' )

def test_modice_filename():
    myEnv = modelEnv.ModelEnv( topDir=topDir )
    assert_equals( myEnv.fixed_filename( type='modice', tileID='h23v05' ),
                   topDir + '/modicev04/MODICE.v0.4.h23v05.3strike.min05yr.mask.nc' )

def test_dem_filename():
    myEnv = modelEnv.ModelEnv( topDir=topDir )
    assert_equals( myEnv.fixed_filename( type='dem', tileID='h23v05' ),
                   topDir + '/SRTMGL3/SRTMGL3.v0.1.h23v05.tif' )
    
def test_basin_filename():
    myEnv = modelEnv.ModelEnv( topDir=topDir )
    assert_equals( myEnv.fixed_filename( type='basin_mask', tileID='h23v05',
                                         drainageID='IN_Indus_at_Kotri' ),
                   topDir + '/basin_masks/IN_Indus_at_Kotri.basin_mask.h23v05.tif' )
    
def test_scag_filename_no_tileID():
    myEnv = modelEnv.ModelEnv( topDir=topDir )
    assert_raises( ValueError, myEnv.forcing_filename, type='modscag_gf' )

def test_scag_filename_no_yyyy():
    myEnv = modelEnv.ModelEnv( topDir=topDir )
    assert_raises( ValueError, myEnv.forcing_filename, type='modscag_gf', tileID='h23v05' )

def test_scag_filename():
    myEnv = modelEnv.ModelEnv( topDir=topDir )
    assert_equals( myEnv.forcing_filename( type='modscag_gf', tileID='h23v05', yyyy=2005 ),
                   topDir + '/MODSCAG_GF/v04/h23v05/MODSCAG_GF_Snow.v0.4.h23v05_2005.h5' )

