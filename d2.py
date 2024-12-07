import numpy as np

# input = np.loadtxt('d2.txt', dtype=int)
input = open("d2.txt","r")

def condition_check(loop_line):
    count = 0
    line = np.array([int(x) for x in loop_line.split()])
    sorted = np.sort(line)
    inverted = np.flip(sorted)

    if np.array_equal(line, inverted) or np.array_equal(line, sorted):
        delta = np.abs(line[1:] - line[:-1])
        if np.max(delta) <= 3 and 0 not in delta: 
            count = 1
    return count 

def alternative_generator(loop_line):
    options = []
    numbers = [x for x in loop_line.split()]

    for i in range(len(numbers)):
        options.append(" ".join(numbers[:i] + numbers[i+1:]))

    return options 


part = 1

count = 0

for loop_line in input:
    output = condition_check(loop_line)
    if output:
        count += 1
        pass
    elif part == 2:
        options = alternative_generator(loop_line)
        for option in options:
            output = condition_check(option)
            if output:
                count += 1
                break
            else:
                pass
    else:
        pass


print(count)


