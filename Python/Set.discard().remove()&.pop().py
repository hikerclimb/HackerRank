n = int(input())
s = set(map(int, input().split()))
for i in range(int(input())):
    operationandvalue = input().split()
    #print('s:' + str(s))
    if operationandvalue[0] == "pop":
        num = s.pop()
    elif operationandvalue[0] == "remove":
        s.remove(int(operationandvalue[1]))
    elif operationandvalue[0] == "discard":
        s.discard(int(operationandvalue[1]))
    
print(sum(s))
