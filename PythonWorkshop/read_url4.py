# Example of reading a bunch of URLs with a for loop

# Load needed libraries

import os
import urllib

# Make sure we're in the project directory

home_dir = os.path.expanduser('~')
work_dir = os.path.join(home_dir, 'projects', 'PythonWorkshop')
try:
    os.chdir(work_dir)
    print "Changed to " + os.getcwd()
except:
    print work_dir + " doesn't seem to exist"

# We want to be able to vary year and month, so we have to break up
# the URL string.  Sometimes you may wish to do this so you can loop
# more easily later.  We're not looping over year, but it will be easier
# if we decide to do so if there is a year variable in what follows.

year = 2012

data = []

# Remember: range stops one before the second number...
for month in range(1,13):
    site = "http://climate.weather.gc.ca"
    # NOTE:  year and month are numbers, so we have to convert to strings
    url = (site + "/climateData/bulkdata_e.html?format=csv&stationID=5415&Year="
        + str(year) + "&Month=" + str(month)
        + "&Day=14&timeframe=1&submit=Download+Data")
    if month == 12:
        url = (site + "/climateData/bulkdata_e.html?format=csv&stationID=5415&Year="
        + str(year-1) + "&Month=" + str(month)
        + "&Day=14&timeframe=1&submit=Download+Data")
    # We use a try to download to catch errors
    try:
        # Create the connector to the site
        download = urllib.urlopen(url)
        # Use the readlines() method to download and append to data
        tmp = download.readlines()
    except:
        print "Something went wrong reading the URL\n%s" % url
    # If we've just got Jan (month = 1), we write the variable names, too
    if month == 1:
        for line in tmp[16:]:
            data.append(line)
    # Otherwise we just write the data
    else:
        for line in tmp[17:]:
            data.append(line)

data_file = str(year) + '.csv'
print "Writing to " + data_file

try:
    with open(data_file, 'w') as f:
        for line in data:
            f.write(line)
except IOError:
    print "ERROR: Unable to open " + data_file + " for writing"
