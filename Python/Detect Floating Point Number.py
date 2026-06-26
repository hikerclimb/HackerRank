import re
T = int(input())
TList = [input() for _ in range(T)]  
for i in TList:
    try:
        mat = bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', i))
        #print(mat)
        #print(mat)
        if mat is True:
            print('True')
        else:
            print('False')
    except:
        #print('enter')
        print('False')
        
