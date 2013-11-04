# Example of reading a URL as a file

# We definitely need a library for this
import urllib

# What's the URL
url = "http://climate.weather.gc.ca/climateData/bulkdata_e.html?format=csv&stationID=5415&Year=2012&Month=11&Day=14&timeframe=1&submit=Download+Data"

# Create the connector to the site
download = urllib.urlopen(url)

# Read the data from the site
data = download.read()

#
#data = data.split("\n")

#for l in data[17:19]:
#    print l