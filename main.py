
import numpy as np #if you don't know its use then I have bad news for you
import matplotlib.pyplot as plot #plotting data in graph
import pandas as pd #for creating and using dataframes
import seaborn as sns #for visualising data uses matplotlib
import calendar #obvious
import os

# import the csv file into a pandas dataframe
df = pd.read_csv('My Uber Drives.csv')
print('Basic manipulation in the data ;) <3'.center(250))
# all the changes made here will be on the DATAFRAME, NOT the CSV file so re-loading will revert the changes

#print(df.head()) # prints first 5 rows and 5 columns of any dataframe

#print(df.tail()) # prints last 5 rows and 5 columns of any dataframe

#print(df.shape)  # prints the shape of the dataframe i.e. the number of rows and columns in the dataframe  Row * Column

#print(df.dtypes) # prints the datatype of each column in the dataframe

#print(df.isnull())

# prints out the dataframe with true or false values for each column i.e. if there is a null value then true else false

#print(df.isnull().sum()) # with .sum at the end we can print out the number of empty values in each column

#print(df[df['PURPOSE*'].isnull()]) # this will print out the rows which have null values in the selected column

#df.drop(df[df['END_DATE*'].isnull()].index,axis=0,inplace=True)
# drops the rows which contain null values axis is for selecting row(0) or column(1)
#print(df.isnull().sum())

#print(df.info()) # prints out the metadata for the dataframe
# the info is needed to be used as a function otherwise data will be printed

# dropping the purpose column as it has a large number of NULL values
#df.drop(['PURPOSE*'],axis=1,inplace=True)

#print(df[df.duplicated()]) #prints out the duplicated record

#df.drop(df[df.duplicated()].index, axis = 0, inplace=True) #removes the row containing duplicate data

# changing the datetime format to datetime from object as it was before
#df['START_DATE*'] = pd.to_datetime(df['START_DATE*'], format='%m/%d/%Y %H:%M')
#df['END_DATE*'] = pd.to_datetime(df['END_DATE*'], format='%m/%d/%Y %H:%M')
# for this to work the total row needs to be dropped as it does NOT have a date and it will give error






