#!/usr/bin/python

# argv[1] File name
# argv[2] File size in MB

import sys
 
with open(sys.argv[1], 'w') as f:
    for i in range(1, int(sys.argv[2]) * (1024 ^ 2)):
        if i % 80 == 0:
            f.write('\n')
        else:
            f.write('a')