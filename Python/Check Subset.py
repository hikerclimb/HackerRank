T = int(input())
for k in range(0,T):
    A = int(input())
    aset = set(input().split())
    B = int(input())
    bset = set(input().split())

    print(aset.issubset(bset))
            
