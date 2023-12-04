file = open("input/input_04.txt")

input = [line.strip("\n").split(": ")[1] for line in file.readlines()]

matches = [len(list(set(filter(None, line.split(" | ")[0].split(" "))).intersection(
    set(filter(None, line.split(" | ")[1].split(" ")))))) for line in input]

games = 0
totalcards = len(input)
scratchcards = [1 if matches[i] > 0 else 0 for i in range(totalcards)]

while sum(scratchcards):
    card_count_index = next((index for index, value in enumerate(scratchcards) if value != 0), None)
    card_count = scratchcards[card_count_index]
    wins = matches[card_count_index]
    for i in range(wins):
        games += card_count
        scratchcards[card_count_index + i + 1] += card_count
    scratchcards[card_count_index] = 0

print(games + totalcards)
