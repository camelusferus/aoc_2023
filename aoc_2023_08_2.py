from math import lcm

file = open("input/input_08.txt")

directions = file.readline().strip('\n')

file.readline()

inputs = {a[0]: (a[2].strip('(),'), a[3].strip('(),')) for a in [line.strip("\n").split() for line in file.readlines()]}

cur = start = [a for a in inputs.keys() if a[2] == 'A']
periods = [0 for i in range(len(cur))]
for i in range(len(cur)):
    steps = 0
    while cur[i][2] != 'Z':
        if directions[steps % len(directions)] == 'L':
            cur[i] = inputs[cur[i]][0]
        else:
            cur[i] = inputs[cur[i]][1]
        steps += 1
    periods[i] = steps

result = 1
for i in periods:
    result = lcm(result, i)

print(result)
