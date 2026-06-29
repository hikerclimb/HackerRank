import re

S= str(input())

pattern = re.compile(r"[aeiouAEIOU]{2,}")
out = re.findall(pattern, S)

if out == []:
    print("-1")
else:
    for i in out:
        print(i)
