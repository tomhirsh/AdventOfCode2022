import numpy as np

num_exec = 100000000
execs = np.zeros(num_exec, dtype=int)

execs[0] = 1
counter = 0
with open('data.txt', 'r') as f:
    for line in f:
        
        line_splitted = line.strip().split(' ')
        
        counter += 1
        if len(line_splitted) == 1:
            continue # noop

        # addx
        v_num = int(line_splitted[1])
        execs[counter + 1] += v_num
        counter += 1

total_strength = 0
x = np.cumsum(execs, 0)
for cycle in range(20, 221, 40):
    strength = cycle * x[cycle-1]
    total_strength += strength

print(total_strength)


# part 2
for i in range(0, 40*6):
    if i % 40 == 0:
        print('')
    if i % 40 in range(x[i]-1, x[i]+2):
        print('#', end='')
    else:
        print('.', end='')
