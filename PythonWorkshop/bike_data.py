# -*- coding: utf-8 -*-
import os
import pandas as pd

# Make sure we're in the project directory

home_dir = os.path.expanduser('~')
work_dir = os.path.join(home_dir, 'projects', 'PythonWorkshop')
try:
    os.chdir(work_dir)
    print "Changed to " + os.getcwd()
except:
    print work_dir + " doesn't seem to exist"

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

# Sometimes the default presentation works and is arguably nicer looking...
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
plt.savefig("bike_data1.png")

# Save it as .eps (vector) file
plt.savefig("bike_data1.eps")

# Let's change the figure size to the legend doesn't obscure the lines
plt.rcParams['figure.figsize'] = (17, 7)

# Any better?
bike_data.plot()
plt.savefig('bike_data2.png')

# Let's plot just two locations
bike_data[['Berri 1', 'Maisonneuve 2']].plot()
plt.savefig('berri_maisonneuve.png')

# Read in the bike_weather data
weather_data = pd.read_csv('./bike_weather.csv', index_col='Date/Time', parse_dates=True)

# Only keep the columns we might actually use
weather_data = weather_data[['Temp (C)', 'Dew Point Temp (C)', 'Rel Hum (%)','Wind Spd (km/h)', 'Visibility (km)', 'Weather']]

# Create a new frame...?
bike_data['Mean Temp'] = weather_data['Temp (C)'].resample('D', how='mean')

# Plot the traffic at Berri 1 and Mean Temp one above the other
bike_data[['Berri 1', 'Mean Temp']].plot(subplots=True)
plt.savefig('berri_and_temp.png')