import numpy as np
import h5py
import sys
import csv
import time
import datetime
import locale
import array
import re
import ConfigParser

# Import Tableau module
import dataextract as tde

h5_file = r'P:\soundcast_2010_soundtransit\branch\soundcast\inputs\daysim_outputs_seed_trips.h5'

my_store = h5py.File(h5_file, "r+")

## Parameters 
tdeFileName = 'csv_extract.tde'

# Read household number from data
daysim_data = np.asarray(my_store['Household']['hhno'])

# Try to create extract, delete if found. 
try:
    tdeFile = tde.Extract(tdeFileName)
except: 
    os.system('del '+tdeFileName)
    os.system('del DataExtract.log')
    tdeFile = tde.Extract(tdeFileName)


# Create TDE table definition
tdeTableDef = tde.TableDefinition() 
 
tdeTableDef.addColumn(k, v)
tdeTable = tdeFile.addTable("Extract",tdeTableDef)