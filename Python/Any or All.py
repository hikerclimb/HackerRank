N = str(input()).split()
palindrome = any((int(x)>int(x+1),  int(x) == int(x), int(x+1) < int(x)) for x in range(len(N) -1) if N > 0)
positiveNumber = all(x >= 0 for x in map(int, input().split()))
print(positiveNumber or palindrome)
