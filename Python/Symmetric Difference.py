import itertools

m = int(input())
mLine = map(int, input().split())
n = int(input())
nLine = map(int,input().split())
out1 = []
nLineSorted = set(sorted(nLine))
mLineSorted = set(sorted(mLine))
out1.append(mLineSorted.difference(nLineSorted))
out1.append(nLineSorted.difference(mLineSorted))
one_d_array = list(itertools.chain.from_iterable(out1))
sortedarray = sorted(one_d_array)
for i in sortedarray:
    print(i)
