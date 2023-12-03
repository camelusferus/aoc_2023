file = open("input/input_03.txt")

input = [line.strip("\n") for line in file.readlines()]

symbols = []
numbers = []
gears = 0

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
            symbols.append({"row": lineno, "col": colno, "sym": char})
        else:
            if num > 0:
                numbers.append({"number": num, "row": lineno, "col": colno - len(str(num))})
                num = 0
        colno += 1
    if num > 0:
        numbers.append({"number": num, "row": lineno, "col": colno - len(str(num))})
        num = 0
    lineno += 1

for number_1 in numbers:
    for number_2 in numbers:
        for symbol in symbols:
            if ((number_1["row"] - 1 <= symbol["row"] <= number_1["row"] + 1) and
                    (number_1["col"] - 1 <= symbol["col"] <= number_1["col"] + len(str(number_1["number"]))) and
                    (number_2["row"] - 1 <= symbol["row"] <= number_2["row"] + 1) and
                    (number_2["col"] - 1 <= symbol["col"] <= number_2["col"] + len(str(number_2["number"]))) and
                    (number_1 != number_2) and symbol["sym"] == "*"):
                gears += number_1["number"] * number_2["number"]

print(str(gears / 2))
