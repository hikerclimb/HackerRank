from itertools import permutations
S, k = input().split()
sorted_items = sorted(S)
string_perms = [''.join(p) for p in permutations(sorted_items, int(k))]
for i in string_perms:
    print(i)
