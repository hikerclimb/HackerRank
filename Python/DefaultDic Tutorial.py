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
    #print('answer:' + str(groupa.get(i)))
    if groupa.get(i) == 'N/A' or groupa.get(i) == None:
        print(-1)
    else:
        for k in groupa.get(i):
            print(k, end=" ")
        print("\n", end="")
