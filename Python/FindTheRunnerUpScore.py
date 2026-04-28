if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    result = list(arr)
    result.sort(reverse=True)
    maxNum = max(result)
    index = 0
    while(True):
        if (result[index] == maxNum):
            while(True):
                if result[index] != result[index+1]:
                    print(result[index+ 1])
                    break
                else:
                    index = index + 1
            break
        else:
            index = index + 1
