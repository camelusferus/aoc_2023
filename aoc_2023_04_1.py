file = open("input/input_04.txt")

input = [line.strip("\n").split(": ")[1] for line in file.readlines()]

matches = [len(list(set(filter(None, line.split(" | ")[0].split(" "))).intersection(
    set(filter(None, line.split(" | ")[1].split(" ")))))) for line in input]

print(sum([2 ** (match - 1) for match in matches if (match > 0)]))
