file = open("input/input_01.txt")

print(sum([10 * int(a[0]) + int(a[-1]) for a in
           [''.join([a for a in s if a.isdigit()]) for s in [line for line in file.readlines()]]]))
