#  Illustrate exception handling and cleanup

import os

data = []

while True:
    try:
        file_name = raw_input("Please enter the name of the file to read:  ")
        with open(file_name) as f:
            print "\nNice.  You named a valid file.  This is what's in it\n"
            for line in f:
                print line,
        break
    except IOError:
        print "\nSorry.  I looked for that file and could not find it"
        print "Please try again\n"
