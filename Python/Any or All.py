def palindrome(S):
    if list(S) == list(S).reverse():
        return True
    else:
        return False

N = str(input())
palindrome = palindrome(N)
positiveNumber = all(x >= 0 for x in map(int, input().split()))
print(positiveNumber and palindrome)
