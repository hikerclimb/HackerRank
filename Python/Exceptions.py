T = input()
for index in range(0,int(T)):
    a,b = input().split()
    try:
        a = int(a)
        b = int(b)  
        print(round(a/b))
    except ValueError as e:
        print('Error Code: ' + str(e))
    except ZeroDivisionError:
        print('Error Code: integer division or modulo by zero')

    
