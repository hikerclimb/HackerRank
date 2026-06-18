from itertools import groupby
S = input()
for k, g in groupby(S, lambda x: x):
    print("(" + str(len(list(g))) + ", " + k + ")"+ " ", end= "")
