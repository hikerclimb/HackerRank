from collections import namedtuple
N = int(input())
columnNames = input().split()
totalGrade = 0
for i in range(0,N):
    data = input().split()
    Storage = namedtuple('StudentRecord', columnNames)
    dataStored = Storage(data[0],data[1], data[2], data[3])
    totalGrade += int(dataStored.MARKS)
average = (totalGrade/N)
print(f"{average:2f}")
