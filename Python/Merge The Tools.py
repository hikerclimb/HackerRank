

def merge_the_tools(string, k):
    numberOfPartitions = int(len(string)/ k)
    j = 0
    prevj = 0
    for i in range(0,numberOfPartitions):
        if len(string) <=9:
            j = i*numberOfPartitions
            numberOfPartitionsDivided = string[j:numberOfPartitions+j]
        elif k ==1:
            numberOfPartitionsDivided = string[i: i+1]
        elif len(string) > 10:
            j = i*int(len(string)/numberOfPartitions)
            prevj = j
            numberOfPartitionsDivided = string[prevj:k*numberOfPartitions]
        print(''.join(list(dict.fromkeys(numberOfPartitionsDivided)))
        .replace(',',"").replace('{', "").replace('}', ""))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
