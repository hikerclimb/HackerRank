S = str(input().split())
m = re.search(r'([a-zA-Z0-9])\1+', S)
if m:
    print(m.group(1))
else:
    print(-1)
