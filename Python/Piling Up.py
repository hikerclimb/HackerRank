T = int(input())
for i in range(0, T):
    n = int(input())
    blocks = list(map(int,input().split()))
    out = ''
    for i in range(0,n -1):
        first = i
        last = n - i - 1
        if len(blocks) == 2:
            out = 'Yes'
        elif len(blocks) == 3 and (blocks[first+1] >= blocks[first] or blocks[last-1] >= blocks[last]):
            out = 'Yes'
        elif blocks[first+1] >= blocks[first] and blocks[last-1] >= blocks[last]:
            out = 'Yes'
        else:
            out = 'No'
    print(out)
