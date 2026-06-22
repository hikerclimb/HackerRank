a = int(input())
aspaceSeperated = set(input().split())
N = int(input())
summation = 0
for i in range(N):
    operation, num = input().split()
    if operation == "intersection_update":
        aspaceSeperated.intersection_update(input().split())
    elif operation == "update":
        aspaceSeperated.update(input().split())
    elif operation == "symmetric_difference_update":
        aspaceSeperated.symmetric_difference_update(input().split())
    elif operation == "difference_update":
        aspaceSeperated.difference_update(input().split())
total = sum(map(int,aspaceSeperated))
print(total)
