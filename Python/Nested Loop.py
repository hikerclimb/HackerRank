dic = {}

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        dic[name] = score
        
    min_val = min(dic.values())
    data = {k: v for k, v in dic.items() if v > min_val}
    sec_min_val = min(data.values())
    datasec = {k: v for k, v in data.items() if v == sec_min_val}
    sorted_dict = dict(sorted(datasec.items()))
    for i in sorted_dict:
        print(i)
