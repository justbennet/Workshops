# Example of reading a bunch of URLs with a for loop

# Load needed libraries

import os
import urllib

# Make sure we're in the project directory

home_dir = os.environ['HOME']
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

year = 2011

# Test case, just the first year.
# NOTE:  range(a,b) is up to but NOT including b
for month in range(1,2):
    site = "http://climate.weather.gc.ca"
    # NOTE:  year and month are numbers, so we have to convert to strings
    url = (site + "/climateData/bulkdata_e.html?format=csv&stationID=5415&Year="
        + str(year) + "&Month=" + str(month)
        + "&Day=14&timeframe=1&submit=Download+Data")

    # This should probably be wrapped in a try...except -- that's for you to
    #    do as an exercise
    # Create the connector to the site
    download = urllib.urlopen(url)

    # Use readlines this time
    data = download.readlines()

    ##### NOTE: data is a list, and each entry in the list has an EOL character
    #####       we can write it directly to a file without adding them
    #####       If we wanted to use them as data right away, we might want
    #####       to get rid of them.
    data_file = str(year) + '-' + str(month) + '.csv'
    print "Writing to " + data_file
    try:
        with open(data_file, 'w') as f:
            for line in data:
                f.write(line)
    except IOError:
        print "ERROR: Unable to open " + data_file + " for writing"
