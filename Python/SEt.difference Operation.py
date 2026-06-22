n = int(input())
nspaceSeperated = list(map(int,input().split()))

b = int(input())
bspaceSeperated = list(map(int,input().split()))

setnspaceSeperated = set(nspaceSeperated)
setbspaceSeperated = set(bspaceSeperated)

out = setnspaceSeperated.difference(setbspaceSeperated)

print(len(out))
