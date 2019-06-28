# OBJECTIVES
# importing csv as data-frame
# using read table of pandas
# reading partial rows of a csv file
# dumping data into a new csv file
# selecting specific columns of a csv file

import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from pandas import read_html

# Section 4##
# File Operation with on TextFile##
# Reading a csv file
dframe = pd.read_csv('demo.csv')
print dframe

# If a .csv file does not have a header it chnges it's first value to a heading
# if the csv file doesn't have a header you can alert the program by
# adding the following line
dframe = pd.read_csv('demo.csv', header=None)
print dframe

# using readtable function
dframe2 = pd.read_table('demo.csv',sep=',')
print dframe2

# importing partial rows gives one the ability to print a few rows instead
# of the whole file
print pd.read_csv('demo.csv',nrows=2)

#dump values to csv
dframe2.to_csv('output.csv', sep=','); # sep=',' can be changed to different values
print "output csv"
print dframe2

# Selecting specific colomns
# the columns should be integers
dframe.to_csv('dataoutput.csv', columns=[0,1])

# Handling Excel Sheets in Python##
excelfile = pd.ExcelFile('Assignment2.xlsx')
dframe = excelfile.parse('Year2008')
# this will look at an individual sheet inside the excel file
print dframe

# Reading HTML with Pandas##
# Scrapping data from an HTML file
# Extract data from a website
url = "https://countrycode.org/"
# a list in python
# package l-xml needs to be installed before running the below line
dflist = pd.io.html.read_html(url)
dframe1 = dflist[0]
print dframe1

print dframe1.columns.values

# Section 5##
# Merging Columns##
# many to one merging
dframe3 = DataFrame({'reference': ['hello', 'goodbye', 'please', 'thanks', 'yes'], 'revenue': [1, 2, 3, 4, 5]})
dframe4 = DataFrame({'reference': ['hello', 'goodbye', 'goodbye', 'hello'], 'revenue': [1, 2, 3, 4]})
print dframe3
print dframe4

dframe5 = pd.merge(dframe3,dframe4,on='reference')
print "MERGE"
print dframe5

dframe6 = pd.merge(dframe3, dframe4, on="reference", how="left")
print dframe6
