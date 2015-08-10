import pandas as pd 
from scipy import stats as stats 

#this is the data from the website

data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''

#this splits lines
data = data.split('\n')

#this splits lines on commas
data = [i.split(', ') for i in data]

#creating the dataframe

column_names = data[0]
data_rows = data[1::]

df = pd.DataFrame(data_rows, columns=column_names)

#changing the dataframes to have float values since the data has decimals 


df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float) 


#renaming the alcohol and tobacco dataframe as df1 and df2
df1 = df['Tobacco']
df2 = df['Alcohol']

#creating a new column which adds the aggregated values from df1 and df2 
df['Combined'] = df1 + df2

#changing df3 to a float 

df['Combined'] = df['Combined'].astype(float)


#defining df-combined as df3
df3 = df['Combined']

#calculating the range

print "The range for the Alcohol and Tobacco dataset is %s, " %(max(df3) - min(df3)) 

#calcualting the mean 

print "The mean for the Alcohol and Tobacco dataset is %s, " %(df3.mean())

#calculating the variance 

print "The variance for the Alcohol and Tobacco dataset is %s, " %(df3.var())

#calculating the standard deviation 

print "The standard deviation for the Alcohol and Tobacco dataset is %s, " %(df3.std())

