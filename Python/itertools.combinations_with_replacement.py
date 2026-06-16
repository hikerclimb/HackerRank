from itertools import combinations_with_replacement
S, k = input().split()
sorted_list = sorted(S)
[print("".join(item)) for item in combinations_with_replacement(sorted_list, int(k))]
