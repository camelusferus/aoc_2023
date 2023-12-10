import functools

file = open("input/input_07.txt")

inputs = [line.strip("\n").split() for line in file.readlines()]

order = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']


def hand_compare(item1, item2):
    for i in range(5, 0, -1):
        if len(item1[i]) > len(item2[i]):
            return -1
        elif len(item1[i]) < len(item2[i]):
            return 1
        elif i == 3 and len(item1[i - 1]) > len(item2[i - 1]):
            return -1
        elif i == 3 and len(item1[i - 1]) < len(item2[i - 1]):
            return 1
        elif len(item1[i]) + len(item2[i]):
            for j in range(5):
                if order.index(item1['hand'][j]) < order.index(item2['hand'][j]):
                    return -1
                elif order.index(item1['hand'][j]) > order.index(item2['hand'][j]):
                    return 1


occurences = [{test_sub: input[0].count(test_sub) for test_sub in order} |
              {'value': int(input[1]), 'hand': input[0]} for input in inputs]

transformed_occurences = [
    {i: [order.index(element) for element in order if occurence[element] == i] for i in range(1, 6)} | {
        'value': occurence['value'], 'hand': occurence['hand'], 'jokers': occurence['J']} for occurence in occurences]

for transformed_occurence in transformed_occurences:
    if transformed_occurence['jokers']:
        for i in range(5, 0, -1):
            if len(transformed_occurence[i]) and transformed_occurence[i] != [12]:
                upgraded_occurence = transformed_occurence[i].pop(0)
                transformed_occurence[i + transformed_occurence['jokers']].append(upgraded_occurence)
                transformed_occurence[transformed_occurence['jokers']].remove(12)
                break

transformed_occurences.sort(key=functools.cmp_to_key(hand_compare), reverse=True)

ranks = 0
for i in range(len(transformed_occurences)):
    ranks += (i + 1) * transformed_occurences[i]['value']

print(ranks)
