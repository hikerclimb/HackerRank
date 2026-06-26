import numpy

def arrays(arr):
    ar = numpy.array(arr[::-1], dtype=float)
    return ar

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
