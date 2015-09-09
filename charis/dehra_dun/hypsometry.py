#!/usr/bin/env python
import csv
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re

class Hypsometry():
    """
    Hypsometry class will read(write) CHARIS hypsometry data from(to) ASCII files.
    Actual hypsometry data will contain the comments from the beginning of the file,
    and a pandas DataFrame.

    2014-09-24 M. J. Brodzik brodzik@nsidc.org 303-492-8263
    National Snow & Ice Data Center, Boulder CO
    Copyright (C) 2014 Regents of the University of Colorado at Boulder
    
    """
    comments = []
    data = pd.DataFrame()

    def __init__( self, comments=[], data=pd.DataFrame(), verbose=False ):
        """
        usage: hyp = hypsometry( comments=[], data=pd.DataFrame(), verbose=False

        Initializer for a CHARIS hypsometry object

        comments : list of strings
        data : pandas DataFrame with elevations in columns and dates in rows
               index can be [None] for undated data, or
               should be a pandas.tseries.index.DatetimeIndex for dated contents

        """
        self.comments = comments
        self.data = data

        # Strip eol characters from the comments
        self.comments = [ line.rstrip( '\r\n' ) for line in self.comments ]

        if verbose:
            print ( __name__ + ": returning new hypsometry object" )
        
    def read( self, filename, verbose=False ):
        """
        usage: hypsometry.read( filename, verbose=False )
        
        Reads elevation by date hypsometry data from filename into a pandas DataFrame.
        
        Assumes file format:
        1) 0 or more comment lines, beginning with '#'
        2) XX number of elevation bands
        3) lower bounds of each elevation band
        4) Data records by date
        """

        # Import the whole file once and
        # Parse the file comments and elevation data first.
        # Elevation data will be used to set pandas column labels
        lines = open( filename ).readlines()
        num_comments = 0
        regex_leading_comment = re.compile( r'#' )
        for line in lines:
            part = regex_leading_comment.match( line )
            if None == part:
                break
            else:
                num_comments += 1
                self.comments.append( line.rstrip( '\r\n' ) )

        # Now use the elevation information to set up column headers
        col_names = [ 'yyyy', 'mm', 'dd', 'doy' ] + lines[ num_comments + 1 ].split()

        # Now read the data part of the file into a DataFrame
        # Use header=None in order to no use anything in the file for the header, and
        # to pass in col_names list for column headers instead.
        # Tell it to skip the comments and the two leading rows before reading real data
        self.data = pd.read_table( filename, sep="\s+", skiprows=num_comments+2,
                              header=None, names=col_names, index_col='doy' )

        # For input data with dates
        # Use the yyyy, mm, dd columns to make a time series index for this DataFrame:
        # otherwise the data are not date-specific, so don't try to make datetime index
        if 999 != self.data.index[ 0 ]:
            date_list = []
            for ( yyyy, mm, dd ) in zip( self.data['yyyy'].values,
                                         self.data['mm'].values,
                                         self.data['dd'].values ):
                date_list.append( dt.date( yyyy, mm, dd ) )
                dates = pd.to_datetime( date_list )
            self.data['Date'] = dates
        else:
            self.data['Date'] = [ None ]
            
        self.data.set_index( [ 'Date' ], inplace=True )
        self.data.drop( [ 'yyyy', 'mm', 'dd' ], axis=1, inplace=True )

        if verbose:
            print ( __name__ + ": read hypsometry data from " + filename )
            print ( __name__ + ": " + str( num_comments ) + " comments." )
            print ( __name__ + ": " + str( len( self.data.index ) ) + " dates." )
            print ( __name__ + ": " + str( len( self.data.columns ) ) + " elevations." )
        
    def write( self, filename, decimal_places=6, verbose=False ):
        """
        usage: hypsometry.write( filename )
        
        Writes elevation by date hypsometry data to filename, formatted for use
        with either CHARIS IDL or python modelling software.  See hypsometry.read
        for file format description.

        If object comments do not begin with '#', then they will be prepended by
        this character in the output file.
        
        """
        fh = open( filename, 'w' )

        # Write any comments first, one comment per line
        regex_leading_comment = re.compile( r'#' )
        regex_trailing_newline = re.compile( r'\n$' )
        for line in self.comments:
            prefix = ''
            suffix = ''
            if None == regex_leading_comment.match( line ):
                prefix = '# '
            if None == regex_trailing_newline.match( line ):
                suffix = '\n'
            fh.write( prefix + line + suffix )

        # Write the number of data columns in the DataFrame
        fh.write( str( len( self.data.columns ) ) + '\n' )

        # Write the elevations for each column, whitespace-separated
        fh.write( ' '.join( self.data.columns ) + '\n' )

        # Close the file so to_csv can now append to it
        fh.close()

        # Make a temporary copy of the DataFrame,
        # and if the data have dates (some do not),
        # add back columns for year, month, day and doy
        tmp = self.data.copy( deep=True )
        if None != tmp.index[ 0 ]:
            tmp[ 'yyyy' ] = tmp.index.year
            tmp[ 'mm' ] = tmp.index.month
            tmp[ 'dd' ] = tmp.index.day
            tmp[ 'doy' ] = tmp.index.dayofyear
        else:
            tmp[ 'yyyy' ] = [ 9999 ]
            tmp[ 'mm' ] = [ 99 ]
            tmp[ 'dd' ] = [ 99 ]
            tmp[ 'doy' ] = [ 999 ]
        tmp = tmp.reindex_axis( [ 'yyyy', 'mm', 'dd', 'doy' ]
                                + list( tmp.columns[:-4] ), axis=1 )

        # Aggravating behavior: if I put a numeral in front of the format decimal place,
        # it will put double-quotes around every floating-point value in the output file
        # no matter what combination of the to_csv switches I use.
        format = "%." + str( decimal_places ) + "f"
        tmp.to_csv( filename, mode='a', header=False, index=False, sep=" ",
                    float_format=format, quoting=csv.QUOTE_NONE )

        # I'm not convinced that this actually frees the tmp variable
        del tmp

        if verbose:
            print ( __name__ + ": wrote hypsometry data to " + filename )
            print ( __name__ + ": " + str( len( self.comments ) ) + " comments." )
            print ( __name__ + ": " + str( len( self.data.index ) ) + " dates." )
            print ( __name__ + ": " + str( len( self.data.columns ) ) + " elevations." )

    def data_by_doy( self, verbose=False ):
        """
        usage: doy_series = hypsometry.data_by_doy()

        Returns a Series object, with the hypsometry data, summed by row (doy).
        """
        if verbose:
            print ( __name__ + ": inside hypsometry.data_by_doy()" )

        return( self.data[ self.data.columns ].sum( axis=1 ) )

        
    
        
    

    
