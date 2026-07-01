import re
N = int(input())
for i in range(0,N):
    S =str(input())
    S.strip()
    pattern = re.compile(":#|#[0-9ABCDEFabcdef]{3}|[0-9ABCDEFabcdef]{6}")
    out = re.findall(pattern, S)
    for j in out:
        print(j)
