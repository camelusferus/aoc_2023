file = open("input/input_01.txt")

textual_numbers = {'on1e': 'one', 'tw2o': 'two', 'th3ree': 'three', 'fo4ur': 'four', 'fi5ve': 'five', 'si6x': 'six',
                   'se7ven': 'seven', 'ei8ght': 'eight', 'ni9ne': 'nine'}

input = [line.strip('\n') for line in file.readlines()]
for pattern in textual_numbers:
    input = [line.replace(textual_numbers[pattern], pattern) for line in input]
print(sum([10 * int(a[0]) + int(a[-1]) for a in [''.join([a for a in s if a.isdigit()]) for s in input]]))