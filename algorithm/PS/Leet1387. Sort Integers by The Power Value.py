def getKth(lo: int, hi: int, k: int):
    answer = []
    for ix in range(lo, hi+1):
        num = ix
        cnt = 0
        while num != 1:
            if num%2 == 0:
                num = num//2
            else:
                num = num*3 + 1
            cnt += 1
        answer.append((ix, cnt))
    
    return sorted(answer, key=lambda l:l[1])[k-1][0]


print(getKth(12, 15, 2))