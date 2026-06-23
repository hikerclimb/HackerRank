N, X = map(int, input().split())
inputList = []
for i in range(0,X):
    inputList.append(list(map(float, input().split())))
transposed = list(zip(*inputList))
total = 0.0 
for i in transposed:
    total = 0
    for j in i:
        total += j
    print(total/X)
