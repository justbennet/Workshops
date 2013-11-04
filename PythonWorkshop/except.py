#  Illustrate exception handling

import os

while True:
try:
        file_name = raw_input("Please enter the name of the file to read:  ")
        fh = open(file_name, 'r')
        break
except IOError:
        print "\nSorry.  I looked for that file and could not find it"
        print "Please try again\n"

print "That file contains these lines:\n"

data = fh.readlines()

print data
