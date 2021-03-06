import os
import re
# Can import just one function from a module
from numpy import sort

# Get to our work directory
home_dir = os.path.expanduser('~')
work_dir = os.path.join(home_dir, 'projects', 'PythonWorkshop')
try:
    os.chdir(work_dir)
    print "Changed to " + os.getcwd()
except:
    print work_dir + " doesn't seem to exist"

# Where our data can be found
file_name = 'matlab.2017-01-08_17:17:45.log'

#####  Define some re patterns here

# A nice guide to the symbolic patterns is at
# http://docs.python.org/2/howto/regex.html
# and can be browsed to in the Canopy Doc Browser,
# Python Documentation -> Python HOWTOs
#  -> Regular Expression HOWTO
# in the section on Simple Patterns

#  Regular expression fields are defined with paretheses and numbered sequentially.
#  You can alternate patterns between captured fields and uncaptured text.  This
#  example uses almost all captured fields.

# Example of a TIMESTAMP line
# 14:30:26 (MLM) TIMESTAMP 6/30/2013
# \d = number; \w = word; + = one or more; TIMESTAMP is literal
timestamp = re.compile(r'(\d{2}:\d{2}:\d{2}) \(\w+\) TIMESTAMP (\d+/\d+/\d+)')
# timestamp.group(1) is the time
# timestamp.group(2) is the date

# Example of a feature checkout line
# 23:09:58 (MLM) OUT: "MATLAB" aquaman@monster.data.umich.edu  
#  NOTE:  There were actually a couple of spaces at the end of the line, so it
#  wasn't matching when the $ terminator was in the re pattern.  Warn people
#  of the dangers of invisibles!
#  Also note the use of escaped parentheses to match text in the input.  In
#  this case, that is part of uncaptured, literal text.
#  mlm_feature = re.compile('(\d{2}:\d{2}:\d{2}) \(MLM\) (\w+): \"(\S+)\" (\w+)@(\S+)$')
mlm_feature = re.compile('(\d{2}:\d{2}:\d{2}) \(MLM\) (\w+): \"(\S+)\" (\w+)@(\S+)')
# mlm_feature(1) is the time
# mlm_feature(2) is OUT|IN
# mlm_feature(3) is the feature name
# mlm_feature(4) is the username
# mlm_feature(5) is the hostname

# Example of a startup line
# 16:55:04 (lmgrd) FLEXnet Licensing (v11.9.0.0 build 87342 x64_lsb) started on checkout.data.umich.edu (linux) (6/3/2013)
lmgrd_start = re.compile('(\d{2}:\d{2}:\d{2}) \(lmgrd\) .* \(linux\) \((\d+/\d+/\d+)\)')
# lmgrd_start.group(1) is start time
# lmgrd_start.group(2) is start date

#####  Those are the regular expressions we need

# List for the log data
data = []

# Dictionary for the feature usage
usage = {}

# Open the file
with open(file_name) as f:
    for line in f:
        # Note that the match() method starts at the beginning and looks
        # forward.
        #
        # Have to put the start line in first to insure that date has a valid
        # value.  No features or timestamps will precede the start.
        if mlm_feature.match(line):
            p = mlm_feature.match(line)
            time = p.group(1)
            feature = p.group(3)
            user = p.group(4)
            host = p.group(5)
            if p.group(2) == 'OUT':
                # print ( "Checked out %s on %s at %s to %s" %
                #    (feature, date, time, user))
                data.append([date, time, feature, user, host])
                try:
                    usage[feature] += 1
                except KeyError:
                    usage[feature] = 1
                except:
                    print "WTF from trying an OUT record...?"
                # Another way to do the above without an exception handler
                # if usage.has_key( feature ): usage[feature] += 1
                # else: usage[feature] = 1
            elif p.group(2) == 'IN':
                # print ( "Checked in %s on %s at %s to %s" %
                #    (feature, date, time, user))
                data.append([date, time, feature, user, host])
                try:
                    usage[feature] -= 1
                except KeyError:
                    usage[feature] = 0
                    print "Just set", feature, "to 0 instead of negative"
                except:
                    print "WTF from trying an IN record...?"
            else:
                # Set p to something that will raise an error if it sneaks through
                p = ''
                pass
            print data[-1][0], data[-1][1], data[-1][2], "current usage is", usage[feature]
        elif timestamp.match(line):
            p = timestamp.match(line)
            time = p.group(1)
            date = p.group(2)
        elif lmgrd_start.match(line):
            # We create a match object, and it has the bits that match
            p = lmgrd_start.match(line)
            # We pull them out and assign them to objects that will persist
            date = p.group(2)
            time = p.group(1)
            print ( "\n\n%-25s %s %s"
                    % ("License server started",date, time) )
            # print "Date changed to: %s at %s" %( date, time)
print "%-25s %s %s" % ("Data ends at", date, time)

print "\n\nHere are the first few lines of data\n"
for i in range(0,20):
    print data[i]

print "\n\nPrinting usages for each feature\n" + "="*32 + '\n'

for key in sort(usage.keys()):
    print "Feature %-25s:  %d" % (key, usage[key])
print "\n\n"
