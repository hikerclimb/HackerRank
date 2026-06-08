

def merge_the_tools(string, k):
    numberOfPartitons = int(len(string)/ k)
    for i in range(0,numberOfPartitons):
        j = i*numberOfPartitons
        if len(string) <=9:
            numberOfPartitionsDivided = string[j:numberOfPartitons+j]
        elif len(string) > 10:
            numberOfPartitionsDivided = string[j:len(string)+j]
        print(''.join(list(dict.fromkeys(numberOfPartitionsDivided)))
        .replace(',',"").replace('{', "").replace('}', ""))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
