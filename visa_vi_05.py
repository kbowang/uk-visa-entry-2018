import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

visa = pd.read_csv("vi_05.csv")



# All columns are non-null objects
# Removed all commas
# Tried to convert columns to int, error showed some cells contain 'z'

# Replaced all 'z' with 0
# Converted all columns to int

# EDIT v1
# Need to try to_numeric


# Grabbing all the years column
visa_converted = visa.iloc[:,2:]

# Finding out the number of 'z' in the columns
visa_converted[visa_converted.loc[:] == 'z'].count()

# Replacing 'z' with '0'
# Created a list to iterate
years = list(visa_converted)

visa_converted[years] = visa_converted[years].replace("z","0")

# Convert to int type
for i in years:
    visa_converted[i] = visa_converted[i].str.replace(",","").astype(int)

# Join cleaned data with the Geographical and Country columns from original data set
visa_new = visa.drop(visa.iloc[:,2:], axis=1).join(visa_converted)

# First 16 rows show the total for each Geographical region
# Can remove this and then create a multilevel index dataframe with region and country

# Drops the first 16 columns
visa_new = visa_new.drop(visa_new.iloc[:17,:].index)

# Need to reset the index
visa_new = visa_new.reset_index()
visa_new = visa_new.drop('index',axis=1)

# Using groupby, created a multilevel index dataframe
visa_grouped = visa_new.groupby(['Geographical region', 'Country of nationality']).sum()
