import os
import re

# Get to our work directory
home_dir = os.path.expanduser('~')
work_dir = os.path.join(home_dir, 'projects', 'PythonWorkshop')
try:
    os.chdir(work_dir)
    print "Changed to " + os.getcwd()
except:
    print work_dir + " doesn't seem to exist"

file_name = 'sample.log'

#####  Define some re patterns here

# Example of a TIMESTAMP line
# 14:30:26 (MLM) TIMESTAMP 6/30/2013
timestamp = re.compile(r'^(\d{2}:\d{2}:\d{2}) \(\w+\) TIMESTAMP (\d+/\d+/\d+)')
# timestamp.group(1) is the time
# timestamp.group(2) is the date

# Example of a feature checkout line
# 23:09:58 (MLM) OUT: "MATLAB" tianfeng@flux-login2.engin.umich.edu  
#  NOTE:  There were actually a couple of spaces at the end of the line, so it
#  wasn't matching when the $ terminator was in the re pattern.  Warn people
#  of the dangers of invisibles!
#  mlm_feature = re.compile('^(\d{2}:\d{2}:\d{2}) \(MLM\) (\w+): \"(\S+)\" (\w+)@(\S+)$')
mlm_feature = re.compile('^(\d{2}:\d{2}:\d{2}) \(MLM\) (\w+): \"(\S+)\" (\w+)@(\S+)')
# mlm_feature(1) is the time
# mlm_feature(2) is OUT|IN
# mlm_feature(3) is the feature name
# mlm_feature(4) is the username
# mlm_feature(5) is the hostname

# Example of a startup line
# 16:55:04 (lmgrd) FLEXnet Licensing (v11.9.0.0 build 87342 x64_lsb) started on flux-license1.engin.umich.edu (linux) (6/3/2013)
lmgrd_start = re.compile('^(\d{2}:\d{2}:\d{2}) \(lmgrd\) .* \(linux\) \((\d+/\d+/\d+)\)')
# lmgrd_start.group(1) is start time
# lmgrd_start.group(2) is start date

#  engin domain to strip it later
engin = re.compile(r'.engin.umich.edu')

data = []

line_no = 0

with open(file_name) as f:
    for line in f:
        line_no += 1
        print "Line %d" % line_no
        # Have to put the start line in first to insure that date has a valid
        # value.  No features or timestamps will precede the start.
        if lmgrd_start.match(line):
            p = lmgrd_start.match(line)
            date = p.group(2)
            time = p.group(1)
            print "License server started on %s at %s" % (date, time)
        elif timestamp.match(line):
            p = timestamp.match(line)
            time = p.group(1)
            date = p.group(2)
            print "Matched timestamp"
        elif mlm_feature.match(line):
            print "Matched feature line"
            p = mlm_feature.match(line)
            time = p.group(1)
            feature = p.group(3)
            user = p.group(4)
            host = p.group(5)
            if p.group(2) == 'OUT':
                print ( "Checked out %s on %s at %s to %s" %
                    (feature, date, time, user))
        else:
            pass
