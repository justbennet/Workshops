import re

#####  Define some re patterns here

# Example of a TIMESTAMP line
# 14:30:26 (MLM) TIMESTAMP 6/30/2013
timestamp = re.compile('^(\d{2}:\d{2}:\d{2}) \(\w+\) TIMESTAMP (\d+/\d+/\d+)')
# timestamp.group(1) is the time
# timestamp.group(2) is the date

# Example of a feature checkout line
# 23:09:58 (MLM) OUT: "MATLAB" tianfeng@flux-login2.engin.umich.edu  
mlm_feature = re.compile(r'^(\d{2}:\d{2}:\d{2}) \(IN|OUT\) (\w+): \"(\S+)\" (\w+)@(\S+)$')
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


for log_line in open('sample.log','r'):

