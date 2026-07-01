import re
N = int(input())


for i in range(0,N):
    Nlines = str(input())
    mat = re.compile(r"^[7|8|9]{1}\d{9}$")
    search = re.search(mat,Nlines)
    
    if search is None:
        print('NO')
    else:
        print('YES')
