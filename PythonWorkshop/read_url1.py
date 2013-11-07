# Example of reading a URL as a file

# Get to our work directory
import os
home_dir = os.path.expanduser('~')
work_dir = os.path.join(home_dir, 'projects', 'PythonWorkshop')
try:
    os.chdir(work_dir)
    print "Changed to " + os.getcwd()
except:
    print work_dir + " doesn't seem to exist"

# We definitely need a library to read data from web sites
import urllib

# What's the URL
url = "http://climate.weather.gc.ca/climateData/bulkdata_e.html?format=csv&stationID=5415&Year=2012&Month=11&Day=14&timeframe=1&submit=Download+Data"

# Create the connector to the site
download = urllib.urlopen(url)

# Read the data from the site
data = download.read()

######
#  Highlight and run just the lines above
#  Now use iPython's ? to see what data is
######

# We can split that one long string with embedded newline characters into
# real lines 
data = data.splitlines()

#######
#  In the python shell window, print the first lines to
#  See where the headers/data begin
#######

output_file = './url1.csv'
# Let's use our tidy way to open files and handle exceptions
try:
    with  open(output_file, 'w') as output_file:
        # Now you know where the boundaries are, fill those into the empty
        # slice below, and write the data to a .csv file
        for l in data[:]:
            output_file.write(l + '\n')
except IOError:
    print "ERROR: " + output_file + " doesn't seem to be creatable."