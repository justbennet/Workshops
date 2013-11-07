# Opening a .csv file

import os
import csv

# Make sure we're in the project directory
home_dir = os.path.expanduser('~')
work_dir = os.path.join(home_dir, 'projects', 'PythonWorkshop')
try:
    os.chdir(work_dir)
    print "Changed to " + os.getcwd()
except:
    print work_dir + " doesn't seem to exist"

# Initialize the data list
data = []

# Reading a .csv file is done with an open file handle, then a csv.reader()
# translates the contents; it's not really a separate file reader

# First, open our data file, which should have been created by read_url3.py
data_file = open('bike_weather.csv', 'r')

# Then set up the csv.reader()
data_reader = csv.reader(data_file)

# Now we have a csv.reader object, which acts like a file/list, so we process
# with a for loop
for row in data_reader:
    data.append(row)

# What do the first rows look like
print "\nThe first 4 rows of data\n"
print data[0:5]
print "\n\n"
# That was very hard to read, but note, each row is a list.  Easier to see
# if you

print "\nPrinting each row individually\n"
for row in range(0,5):
    print data[row]
    print "\n"
print "\n\n"

# Finally, we add a second index (position indicator) to get specific
# values off each row.  Here, we get the first four rows of data, each
# is a list, and from each of those lists, we get the first and seventh
# (remember we start counting at 0, so item 6 is the seventh thing),
# and we print that value as it was read, as well as converting it to
# a number, calculating something with it, then printing the result.
# The data we read is all strings, so we need to convert to a floating
# point (decimal) number before doing arithmetic.

for i in range(1,5):
    print ("Date is %s and temperature is %s degrees C, %4.2f degrees F" %
       (data[i][0], data[i][6], 9 * float(data[i][6])/5 + 32))

# Create a new data set that contains just the Date/Time, Temp (C),
# Wind Spd (km/h), and Weather.

# We'll need a new, empty list
n = []

# We need to read each line, the create a new list with just the elements
# from the old we want.  Uncomment and complete the code below so it does
# that.

# for line in data:
#     subset = ...
#     n.append(subset)
#
# print "\nFirst few rows of the subset\n"
# for row in range(0,5):
#     print n[row]
