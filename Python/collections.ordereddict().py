from collections import OrderedDict

N = int(input())
ordered_dictionary = OrderedDict()
nameswithordered_dictionary = OrderedDict()
namesAndCost = []
for i in range(0,N):
    namesAndCost.append(input().split())
    if str(namesAndCost[i][1]).isalpha() is True:
        key = namesAndCost[i][0] + ' ' + namesAndCost[i][1]
        ordered_dictionary[key] = ordered_dictionary.get(key, 0) + 1
    else: 
        key = namesAndCost[i][0]
        ordered_dictionary[key] = ordered_dictionary.get(key, 0) +1 
for j in range(0, N):
    if namesAndCost[j][1].isalpha() is True:
        key = namesAndCost[j][0] + ' ' + namesAndCost[j][1]
        nameswithordered_dictionary[key] = int(ordered_dictionary[key]) * int(namesAndCost[j][2])
    else: 
        key = namesAndCost[j][0]
        nameswithordered_dictionary[key] = int(ordered_dictionary[key]) * int(namesAndCost[j][1])
for orderedDictKey, orderedDictValue in nameswithordered_dictionary.items():
    print(orderedDictKey + ' ' + str(orderedDictValue))



