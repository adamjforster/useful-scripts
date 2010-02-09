#!/usr/bin/python2.6

import sys

with open(sys.argv[1]) as f:
    line_number = 1
    file_number = 1
    
    output_file = open(sys.argv[1] + str(file_number), 'w')
                       
    for line in f:
        output_file.write(line)
        
        if line_number % int(sys.argv[2]) == 0:
            output_file.close()
            file_number += 1
            output_file = open(sys.argv[1] + str(file_number), 'w')
        line_number += 1
    
    output_file.close()