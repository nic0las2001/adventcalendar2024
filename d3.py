import numpy as np
import re

# input = np.loadtxt('d2.txt', dtype=int)
input = open("d3.txt","r")

sum = 0
part = 2
do = True

if part == 1:
    for line in input:
        for i in range(len(line)):
            if re.match(r"mul\(\d+,\d+\)", line[i:]):
                first_bracket = line[i:].index(")") + i
                vals = re.findall(r"\d+", line[i:first_bracket])
                sum += int(vals[0]) * int(vals[1])
else:
    for line in input:
        for i in range(len(line)):
            if re.match(r"mul\(\d+,\d+\)", line[i:]):
                first_bracket = line[i:].index(")") + i
                vals = re.findall(r"\d+", line[i:first_bracket])
                if do:
                    sum += int(vals[0]) * int(vals[1])
            elif re.match(r"do\(\)",line[i:]):
                do = True
            elif re.match("don\'t\(\)",line[i:]): 
                do = False

print(sum)