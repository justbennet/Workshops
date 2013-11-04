import os

### Read in a file and print the contents

# Import the os module so its funcions are available to us
import os

# Where is our home directory?
home_dir = os.environ['HOME']

# Change to the Workshop folder under it
os.chdir(os.path.join(home_dir, "projects", 'PythonWorkshop'))

os.getcwd() # Print where we are, just to be sure

# Assign the name of our data file to a variable
filename = '2011.csv'

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
for i in range(0,11):
    print data[i]

# print the last line
print data[-1]

# Another way to read the file...

# Reopen the file
data_file = open(filename, 'r')

# Use a list comprehension to read the data
date = [ l.strip() for l in data_file ]

# Exercise: rewrite the list comprehension as a for
