#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = input()
    my_dict = {}
    for ch in s:
        if ch not in my_dict:
            my_dict[ch]=0 
        my_dict[ch] += 1

sorted_items = sorted(my_dict.items(), key=lambda x: (-x[1], x[0]))

# Print the top 3 items
for item, count in sorted_items[:3]:
    print(f"{item} {count}")   
