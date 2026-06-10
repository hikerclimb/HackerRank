from collections import Counter

X = int(input())
counterShoeSizeInShop = Counter(map(int, input().split()))
N = int(input())

summ = 0
for i in range(0,N):
    shoeSize, price = map(int, input().split())
    if counterShoeSizeInShop[shoeSize] > 0:
        summ += price
        counterShoeSizeInShop[shoeSize] -= 1
        
print(summ)
