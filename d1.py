import numpy as np

input = np.loadtxt('d1.txt', dtype=int)

# Part 1
l1 = input[:,0]
l2 = input[:,1]
l1.sort(); l2.sort()
delta = abs(l2 - l1)
total = np.sum(delta)
print(total)

# Part 2
score = 0
for number in l1:
    tempscore = 0
    for number2 in l2:
        if number2 == number:
            tempscore += 1
        
    tempscore *= number
    score += tempscore

print(score)