### Read in a file and print the contents

# Import the os module so its funcions are available to us
import os

# Where is our home directory?
home_dir = os.environ['HOME']

# Change to the Workshop folder under it
os.chdir(os.path.join(home_dir, 'Workshop'))

os.getcwd() # Print where we are, just to be sure

# Assign the name of our data file to a variable
filename = 'hello.txt'

# Open the file
data_file = open(filename, 'r')

# Read its contents
data = data_file.readlines()

# Be tidy and close the file
data_file.close()

# Print a header...
print "These are the lines from %s" % filename
print "=" * 34
# ...and the data
print "%s" % data