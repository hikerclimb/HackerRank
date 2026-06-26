import re
T = int(input())
TList = [input() for _ in range(T)]  
for i in TList:
    try:
        mat = bool(re.match(r"[-\+\d\.]*\d.*", i))
        print(mat)
        #print(mat)
        if mat is True:
            print('True')
        else:
            print('False')
    except:
        print('enter')
        #print('False')
        
