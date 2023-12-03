file = open("input/input_03.txt")

input = [line.strip("\n") for line in file.readlines()]

symbols = []
numbers = []
active_numbers = []

lineno = 0

for line in input:
    colno = 0
    num = 0
    for char in line:
        if char.isdigit():
            num = num * 10 + int(char)
        elif char != '.':
            if num > 0:
                numbers.append({"number": num, "row": lineno, "col": colno - len(str(num))})
                num = 0
            symbols.append({"row": lineno, "col": colno})
        else:
            if num > 0:
                numbers.append({"number": num, "row": lineno, "col": colno - len(str(num))})
                num = 0
        colno += 1
    if num > 0:
        numbers.append({"number": num, "row": lineno, "col": colno - len(str(num))})
        num = 0
    lineno += 1

for number in numbers:
    for symbol in symbols:
        if ((number["row"] - 1 <= symbol["row"] <= number["row"] + 1) and
                (number["col"] - 1 <= symbol["col"] <= number["col"] + len(str(number["number"])))):
            active_numbers.append(number)

active_numbers = [i for n, i in enumerate(active_numbers) if i not in active_numbers[n + 1:]]

active_numbers_sum = sum([n["number"] for n in active_numbers])

print(active_numbers_sum)
