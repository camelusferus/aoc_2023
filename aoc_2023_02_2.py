file = open("input/input_02.txt")

input = [line.strip("\n") for line in file.readlines()]
cubes = 0

for line in input:
	red = green = blue = 0
	games = line.split(": ")[1].split("; ")
	for game in games:
		colours = {cube.split(" ")[1]:cube.split(" ")[0] for cube in game.split(", ")}
		if ("red" in colours) and (int(colours["red"]) > red):
			red = int(colours["red"])
		if ("green" in colours) and (int(colours["green"]) > green):
			green = int(colours["green"])
		if ("blue" in colours) and (int(colours["blue"]) > blue):
			blue = int(colours["blue"])
	cubes += (blue * green * red)

print(cubes)
