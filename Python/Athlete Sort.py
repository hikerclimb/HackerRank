#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    removed_matrix = [[str(sub_item) for sub_item in item]for item in arr]
    sorted_matrix = sorted(arr, key=lambda row: int(row[k]))

    #print(sorted_matrix)
    for i in sorted_matrix:
        for j in i:
            print(str(j).replace(',', '').replace('[[', '').replace(']]', '').replace('[', '').replace(']', '').replace('\'', ''), end=" ")
        print()
