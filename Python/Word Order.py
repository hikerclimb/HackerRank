from collections import Counter

n = int(input())
diction = Counter()
for l in range(0,n):
    line = input()
    diction[line] += 1
print(len(diction))
for key,value in diction.items():
    print(value, sep= " ", end= " ")
