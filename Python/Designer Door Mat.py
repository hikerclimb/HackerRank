if __name__ == '__main__':
    inpu = input()
    N, M= inpu.split(' ')
    N = int(N)
    M = int(M)
    for i in range(1,int(N), 2):
        print(('.|.'*i).center(M, '-'))
    print('WELCOME'.center(M, '-'))
    for i in range(int(N-2), 0, -2):
        print(('.|.'*i).center(M, '-'))
