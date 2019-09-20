#!/usr/bin/env python

"""
Clean an Excel file which contains the skills of consultants. Remove redundant characters, white spaces and duplicate skills. Export to Excel sheet.
"""

import pandas as pd
import numpy as np
from pandas import ExcelWriter
from pandas import ExcelFile

_author__ = "Aadam Bari"
__maintainer__ = "Aadam Bari"
__email__ = "aadambari@msn.com"
__status__ = "Prototype"



s = pd.read_excel('test.xlsx',columns=0, squeeze=True) # read excel into Series

s = s.str.strip('[]') # remove square brackets
s = s.str.replace('"', '') #remove double quotes
s.replace('', np.nan, inplace=True) # remove empty space with null values 
s.dropna(inplace=True) # remove null values / empty rows
s.reset_index(drop=True,inplace=True) #reset indexes

# print (s)

skillsLists = s.str.split(",").tolist() # split skills and add to list
flattened_list = [y for x in skillsLists for y in x] # flatten list

# print(flattened_list)

flattened_list = list(dict.fromkeys(flattened_list)) #remove duplicate values

skills_series = pd.Series(flattened_list) # convert lists of skills into a pandas Series

# write to excel
skills_series.to_excel("output.xlsx", index=False)

