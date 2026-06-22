n = int(input())
nspaceSeperated = list(map(int,input().split()))

b = int(input())
bspaceSeperated = list(map(int,input().split()))

setnspaceSeperated = set(nspaceSeperated)
setbspaceSeperated = set(bspaceSeperated)
 
out = setnspaceSeperated.symmetric_difference(setbspaceSeperated)

print(len(out))
