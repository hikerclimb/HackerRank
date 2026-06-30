import re

S= str(input())

pattern = re.compile(r"(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])[aeiouAEIOU]{2,}(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])")
out = re.findall(pattern, S)

if out == []:
    print("-1")
print('\n'.join(out))
