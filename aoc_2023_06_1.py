file = open("input/input_06.txt")

input = [line.strip("\n").split(":")[1] for line in file.readlines()]

dates = [[int(input[0].split()[i]),int(input[1].split()[i])] for i in range(len(input[0].split()))]
ways_to_beat = 1

for date in dates:
    record_beaten = 0
    for i in range(1,date[0]):
        if (date[0]-i)*i > date[1]:
            record_beaten += 1
    ways_to_beat *= record_beaten

print(ways_to_beat)
