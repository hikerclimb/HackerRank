from collections import defaultdict
n, m = input().split()
groupa = defaultdict(list)
for i in range(1, int(n)+1):
    items = input()
    groupa[str(items)].append(str(i))

groupb = list()
for j in range(int(n) , int(m)+ int(n)):
    items = input()
    groupb.append(items)

out = list()

for i in groupb: 
    out.append(groupa.get(i))
for j in out:
    print(' '.join(j))
