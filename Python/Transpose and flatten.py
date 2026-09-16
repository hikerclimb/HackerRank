import numpy as np

arr = []
N, M = map(int,input().split())
for i in range(0, N):
    arr.append(list(input().split()))
#print(arr)
out = np.array(arr)
int_out = out.astype(int)
flatten = int_out.flatten()
transpose = np.transpose(int_out)
print(transpose)
print(flatten)
