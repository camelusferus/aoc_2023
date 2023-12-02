file = open("input/input_02.txt")

input = [line.strip("\n") for line in file.readlines()]
valids = 0

for line in input:
	valid = 1
	id = int(line.split(": ")[0].split(" ")[1])
	games = line.split(": ")[1].split("; ")
	for game in games:
		colours = {cube.split(" ")[1]:cube.split(" ")[0] for cube in game.split(", ")}
		if ("red" in colours) and (int(colours["red"]) > 12):
			valid = 0
		if ("green" in colours) and (int(colours["green"]) > 13):
			valid = 0
		if ("blue" in colours) and (int(colours["blue"]) > 14):
			valid = 0
	valids += valid*id

print(valids)
