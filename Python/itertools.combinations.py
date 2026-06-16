from itertools import combinations

input, k = input().split()
sorted_list = sorted(input)
out = ""
for i in range(1,int(k)+1):
    [print("".join(item)) for item in combinations(sorted_list, int(i))]
