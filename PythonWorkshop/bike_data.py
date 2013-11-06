# -*- coding: utf-8 -*-
import pandas as pd

# Read the data, csv, we have some accented characters
bike_data = pd.read_csv("./bike_data.csv", encoding='latin1', sep=';',
                        index_col='Date', parse_dates=True, dayfirst=True)

pd.set_option('display.line_width', 80)

# Look at the first 10 observations
print bike_data.head()

# Descriptive statistics for same
print bike_data.describe()

# Drop the variables (columns) where there are no valid values, i.e., Brébeuf
# and St-Urbain; note axis 0 is rows, axis 1 is columns.
bike_data = bike_data.dropna(axis=1)
print bike_data.head(n=10)

# We can look at just some columns by specifying their names in a list
# Note the u'..' for the string with the accented character
print bike_data[['Berri 1', u'Côte-Sainte-Catherine', 'Maisonneuve 1']].head()

# Sometimes the default presentaion works...
bike_data[['Berri 1', u'Côte-Sainte-Catherine', 'Maisonneuve 1']].head()


# Or by specifying their column numbers
print bike_data[[0,1,2]].head()

# Making plots is pretty easy, too, if you are willing to accept the default
# layout and formatting

# We need to make sure we have the plotting module loaded
import matplotlib.pyplot as plt

# Just plot the data against the date index
bike_data.plot()
# You probably want to save some figures.  The savefig() method knows which
# graphics format to use based on the extension you give it

# Save it as a .png (raster) file
plt.savefig("bike_data.png")

# Save it as .eps (vector) file
plt.savefig("bike_data.eps")

# Let's change the figure size to the legend doesn't obscure the lines
plt.rcParams['figure.figsize'] = (17, 7)

# Any better?
bike_data.plot()

# Let's plot just two locations
bike_data[['Berri 1', 'Maisonneuve 2']].plot()
