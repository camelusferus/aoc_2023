file = open("input/input_08.txt")

directions = file.readline().strip('\n')

file.readline()

inputs = {a[0]: (a[2].strip('(),'), a[3].strip('(),')) for a in [line.strip("\n").split() for line in file.readlines()]}

cur = start = 'AAA'
stop = 'ZZZ'
steps = 0

while cur != stop:
    if directions[steps % len(directions)] == 'L':
        cur = inputs[cur][0]
    else:
        cur = inputs[cur][1]
    steps += 1

print(steps)
