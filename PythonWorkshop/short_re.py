import os
import re
# Can import just one function from a module
from numpy import sort

# Example of a feature checkout line
# 23:09:58 (MLM) OUT: "MATLAB" aquaman@monster.data.umich.edu  
#  NOTE:  There were actually a couple of spaces at the end of the line, so it
#  wasn't matching when the $ terminator was in the re pattern.  Warn people
#  of the dangers of invisibles!
#  mlm_feature = re.compile('(\d{2}:\d{2}:\d{2}) \(MLM\) (\w+): \"(\S+)\" (\w+)@(\S+)$')
mlm_feature = re.compile('(\d{2}:\d{2}:\d{2}) \(MLM\) (\w+): \"(\S+)\" (\w+)@(\S+)')
# mlm_feature(1) is the time
# mlm_feature(2) is OUT|IN
# mlm_feature(3) is the feature name
# mlm_feature(4) is the username
# mlm_feature(5) is the hostname

data = []

line = '23:09:58 (MLM) OUT: "MATLAB" aquaman@monster.data.umich.edu  '

p = mlm_feature.match(line)
# See definition of mlm_feature RE for what the elements are
data.append([ p.group(i) for i in range(1,6) ])
