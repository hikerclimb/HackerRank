from itertools import groupby
S = input()
for k, g in groupby(S):
    print("(" + str(len(list(g))) + ", " + k + ")"+ " ", end= "")
