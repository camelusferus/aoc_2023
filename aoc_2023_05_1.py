file = open("input/input_05.txt")

input = [line for line in file.read().strip("\n").split("\n\n")]

def create_transformation_map(input_string):
    return [{'dest_start': int(transforma.split()[0]), 'source_start': int(transforma.split()[1]), 'length': int(transforma.split()[2])} for transforma in input_string]


seeds = input[0][7:].split()
transform_maps = [create_transformation_map(input[i].split("\n")[1:]) for i in range(1,8)]
locations = []

for seed in seeds:
    transform_location = int(seed)
    for i in range(7):
        for j in range(len(transform_maps[i])):
            if 0 <= transform_location - transform_maps[i][j]["source_start"] < transform_maps[i][j]["length"]:
                transform_location = transform_location - transform_maps[i][j]["source_start"] + transform_maps[i][j]["dest_start"]
                break
    locations.append(transform_location)

print(min(locations))
