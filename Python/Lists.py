lis = []
if __name__ == '__main__':
    N = int(input())
    
    for _ in range(N):
        command = input().split()
        cmd_name = command[0]
        if cmd_name == "insert":
            lis.insert(int(command[1]), int(command[2]))
        elif cmd_name == "print":
            print(lis)
        elif cmd_name == "remove":
            lis.remove(int(command[1]))
        elif cmd_name ==  "append":
            lis.append(int(command[1]))
        elif cmd_name == "sort":
            lis = [int(x) for x in lis]
            lis.sort(reverse=False) 
        elif cmd_name == "pop":
            lis.pop()
        elif cmd_name == "reverse":
            lis.reverse()
