import sys

with open(sys.argv[1]) as f:
    output_file = open(sys.argv[1] + '-joined', 'w')
    for line in f:
        output_file.write(line.replace('\n', ' '))
    output_file.close()
