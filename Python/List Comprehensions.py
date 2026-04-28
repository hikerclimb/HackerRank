if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print('[',  sep=' ', end='', flush=True)
    [print('[' + str(xnum) + ', ' + str(ynum) + ', ' + str(znum) + '] ,',  sep=' ', end='', flush=True) for xnum in range(0, x+1) for ynum in range(0,y+1) for znum in range(0,z+1) if xnum + ynum + znum != n]
    print(']')
