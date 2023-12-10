file = open("input/input_09.txt")

sensors_history = [[[int(a) for a in line.strip("\n").split()]] for line in file.readlines()]

for history in sensors_history:
    while sum(history[-1]) != 0 or len(history) == 1:
        history.append([history[-1][i+1]-history[-1][i] for i in range(len(history[-1])-1)])

    for i in range(len(history)-2,-1,-1):
        history[i].insert(0,history[i][0] - history[i+1][0])

print(sum([sensor[0][0] for sensor in sensors_history]))