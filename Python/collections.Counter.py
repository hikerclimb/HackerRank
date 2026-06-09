from collections import Counter

# Enter your code here. Read input from STDIN. Print output to STDOUT
X = int(input())
shoeSizeInShop = list(map(int, input().split()))
N = int(input())
shoesSizeWantedAndPrice = []
for size in range(0,N):
    shoesInfo = (list(map(int, input().split())))
    shoesSizeWantedAndPrice.append(tuple(shoesInfo))
counterOfShoeSizeAndPrice = Counter(shoesSizeWantedAndPrice)
summ = 0
for item, frequency in counterOfShoeSizeAndPrice.items():
    #print('i:'+str(i))
    for i in range(0, X):
        if item[0] == shoeSizeInShop[i]:
            #print(str(item[0]) + ':' + str(item[1]))
            #print(shoeSizeInShop[i])
            summ += item[1]
            break
print(summ)
