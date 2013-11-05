#  Illustrate exception handling

import os
import sys

try:
    file_name = raw_input("Please enter the name of the file to read:  ")
    fh = open(file_name, 'r')
except IOError:
    print "\nSorry.  I looked for that file and could not find it"
    sys.exit()

# It's more correct to write a main() function, then exit the function, but
# that's really beyond the scope of what we're doing here.  There is an article
# by Python's creator at
# http://www.artima.com/weblogs/viewpost.jsp?thread=4829
# for those who want to explore that

print "That file contains these lines:\n"

data = fh.readlines()

print data
