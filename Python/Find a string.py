def count_substring(string, sub_string):
    counter =0
    i = 0
    while(string.find(sub_string) != -1 ):
        startPosition = string.find(sub_string)
        if string[startPosition] == sub_string[i]:
            counter = counter + 1
            i = i + 1
        string = string[startPosition+len(sub_string)-1:]
        i = 0
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
