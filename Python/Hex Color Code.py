import re
N = int(input())
S = ""
for i in range(0,N):
    S +=str(input())
    S.strip()
    
pattern = re.compile(r"{(.*?)}")
match = re.findall(pattern, S)
pattern2 = re.compile(r"[#][0-9ABCDEFabcdef]{3,6}")
out = []
for j in match:
    out.append(re.findall(pattern2, j))
for j in out:
    for i in j:
        print(i, sep="\n")
