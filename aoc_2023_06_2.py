file = open("input/input_06.txt")

dates = [int(''.join(line.strip("\n").split(":")[1].split())) for line in file.readlines()]

print(sum([1 if ((dates[0]-i)*i > dates[1]) else 0 for i in range(1,dates[0])]))
