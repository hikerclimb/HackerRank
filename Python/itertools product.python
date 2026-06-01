from itertools import product

list1 = [int(x) for x in input().split()]
list2 = [int(x) for x in input().split()]

clean_list1 =  [x for x in list1 if x != ' ' ]
clean_list2 =  [x for x in list2 if x != ' ' ]

out = product(clean_list1, clean_list2)

clean_list = list(out)

print(" ".join(str(x) for x in clean_list))
