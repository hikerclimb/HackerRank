n, m  = input().split()
nintegers = input().split()
mintegersA = set(input().split())
mintegersB = set(input().split())

totalhappiness = 0
for i in nintegers:
    if i in mintegersA:
        totalhappiness += 1
    elif i in mintegersB:
        totalhappiness -= 1
print(totalhappiness)
