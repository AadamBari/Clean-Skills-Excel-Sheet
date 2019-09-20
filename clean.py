# Program to extract number 
# of rows using Python 
# import xlrd 

# # # Give the location of the file 
# loc = ("Skills.xlsx") 

# wb = xlrd.open_workbook(loc) 
# sheet = wb.sheet_by_index(0) 
# sheet.cell_value(0, 0) 

# # # Extracting number of rows 
# print(sheet.nrows) 



import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.read_excel('test.xlsx',columns=0, squeeze=True)

# for index, row in df.iterrows():
#     print (row)

df = df.str.strip('[]')
df = df.str.replace('"', '')
# print (df)
df.to_excel("output.xlsx", index=False)
