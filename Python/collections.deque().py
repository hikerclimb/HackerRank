from collections import deque
N_operations = int(input())
deq = deque()
for i in range(0, N_operations):
    operationAndNum = input().split()
    if operationAndNum[0] == 'append':
        deq.append(operationAndNum[1])
    elif operationAndNum[0] == 'appendleft':
        deq.appendleft(operationAndNum[1])
    elif operationAndNum[0] == 'pop':
        deq.pop()
    elif operationAndNum[0] == 'popleft':
        deq.popleft()
for j in deq:
    print(j, sep = " ", end= " ")
 
 
