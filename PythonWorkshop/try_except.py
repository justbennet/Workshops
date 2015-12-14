#  Illustrate exception handling and cleanup

import os

# Make sure we're in the project directory
home_dir = os.path.expanduser('~')
work_dir = os.path.join(home_dir, 'projects', 'PythonWorkshop')
try:
    os.chdir(work_dir)
    print "Changed to " + os.getcwd()
except:
    print work_dir + " doesn't seem to exist"

data = []

# An example of getting input from the command line using a while loop
while True:
    try:
        file_name = raw_input("Please enter the name of the file to read:  ")
        if file_name == '':
            print "\n\nOK, OK!  I quit..."
            break
        # with will automatically close the file after the read.  Nice!
        with open(file_name) as f:
            print "\nNice.  You named a valid file.  This is what's in it\n"
            for line in f:
                print line,
        break
    except IOError:
        print "\nSorry.  I looked for that file and could not find it\n"
        print "Please try again\n"
    except KeyboardInterrupt:
        print "\n\nOK, OK!  I quit..."
        break
    except EOFError:
        print "\n\nOK, OK!  I really quit..."
        break
