import json
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    out = ''
    out += '['
    [out := '[' + str(xnum) + ' , ' + str(ynum) + ' , ' + str(znum) +' ],' +out for xnum in range(0, x+1) for ynum in range(0,y+1) for znum in range(0,z+1) if xnum + ynum + znum != n]
    out = ''.join(("[",out))
    out = out[:-2]
    out += ']'
    jsonLoad = json.loads(out)
    jsonLoad = jsonLoad[::-1]

    print(jsonLoad)
