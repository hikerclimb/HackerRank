A = set(input().split())
n = int(input())
out = False
for i in range(0,n):
    #print(i, n -1)
    out = A.issuperset(set(input().split()))
    if out is False:
        print('False')
        break
if out is True:
    print('True')
