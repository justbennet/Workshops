### Read in a file and print the contents

# Import the os module so its funcions are available to us
import os

# Where is our home directory?
home_dir = os.path.expanduser('~')

# Change to the Workshop folder under it
os.chdir(os.path.join(home_dir, "projects", 'PythonWorkshop'))

os.getcwd() # Print where we are, just to be sure

# Assign the name of our data file to a variable
filename = 'bike_weather.csv'

# Open the file
data_file = open(filename, 'r')

# Initialize a list for the data
data = []

# Read its contents with a for loop
for line in data_file:
    data.append(line)

# Be tidy...
data_file.close()

# Print some data lines... how many?  How does range() work?
print "Printing some data lines\n"
for i in range(0,6):
    print data[i]
    print "\n"

# print the last line
print "Printing the last few lines\n"
print data[-5:]
print "\n"

# Another way to read the file...

# Reopen the file
data_file = open(filename, 'r')

# Use a list comprehension to read the data, makes it easy to apply a
# function/method to the elements of the list.
data = [ l.strip() for l in data_file ]

data_file.close()

# Exercise: rewrite the list comprehension as a for loop to make sure you
# understand how it works and how to get the strip() method applied
