def solution(n, m):
    answer = []
    div_n = {}
    div_m = {}
    for ix in range(2, n + 1):
        while True:
            if n%ix == 0:
                n = n//ix
                if ix in div_n:
                    div_n[ix] += 1
                else:
                    div_n[ix] = 1
            else:
                break

    for ix in range(2, m + 1):
        while True:
            if m%ix == 0:
                m = m//ix
                if ix in div_m:
                    div_m[ix] += 1
                else:
                    div_m[ix] = 1
            else:
                break

    min = 1
    max = 1
    for div in div_n:
        if div in div_m:
            if div_n[div] > div_m[div]:
                min *= pow(div, div_m[div])
                max *= pow(div, div_n[div])
            else:
                min *= pow(div, div_n[div])
                max *= pow(div, div_m[div])
        else:
            max *= pow(div, div_n[div])

    for div in div_m:
        if div not in div_n:
            max *= pow(div, div_m[div])

    return [min, max]

print(solution(3, 12))