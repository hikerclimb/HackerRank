if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    output = [[xnum,ynum,znum] for xnum in range(x+1) for ynum in range(y+1) for znum in range(z+1) if xnum + ynum + znum != n ]
    print(output)
