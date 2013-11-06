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
data_file = open('2011.csv', 'r')

# Then set up the csv.reader()
data_reader = csv.reader(data_file)

# Now we have a csv.reader object, which acts like a file/list, so we process
# with a for loop
for row in data_reader:
    data.append(row)

# What do the first rows look like
print "The first 4 rows of data"
print data[0:5]

# That was very hard to read, but note, each row is a list.  Easier to see
# if you
for row in range(0:5):
    print data[row]

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
       (data[i][0], data[i][6], 9*float(data[i][6])/5 + 32))

