# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    inpu = input()
    N, M= inpu.split(' ')
    N = int(N)
    M = int(M)
    counter = 1
    sub = 0
    for i in range(int(N/2)):
        for j in range(int(M/2)-(counter+sub)):
            print('-', end="")
        for k in range(counter):
            print('.|.', end="")
        for l in range(int(M/2)- (counter+sub)):
            print('-', end="")
        counter = counter +2
        sub =sub +1
        print('\n', end="")
        
    sub = 0
    for m in range(int(N+ sub)):
        print('-', end= "")
    print('WELCOME', end="")
    for m in range(int(N+sub)):
        print('-', end="")
    print("")
        
        
    counter = round(N/M) +5
    sub = 2
    for i in range(int(N/2)):
        for j in range(round(M/2)- (counter + sub)):
            print('-', end="")
        for k in range(counter):
            print('.|.', end="")
        for l in range(round(M/2)- (counter + sub)):
            print('-', end="")
        counter = counter - 2
        sub= sub -1
        print('\n', end="")
        
