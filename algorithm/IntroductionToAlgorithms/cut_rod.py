import sys
import time

p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]*2

def cut_rod(p, n):
    if n is 0:
        return 0
    q = -sys.maxsize
    for i in range(0, n):
        q = max(q, p[i] + cut_rod(p, n-(i+1)))
    return q

def memoized_cut_rod_aux(p, n, r):
    if r[n-1] >= 0:
        return r[n-1]

    if n is 0:
        q = 0
    else:
        q = -sys.maxsize
        for i in range(0, n):
            q = max(q, p[i]+memoized_cut_rod_aux(p, n-(i+1), r))
    r[n-1] = q
    return q

def memoized_cut_rod(p, n):
    r = [-sys.maxsize]*len(p)
    return memoized_cut_rod_aux(p, n, r)

s_time = time.time()
print(cut_rod(p, len(p)))
print("time : ",time.time() - s_time)

s_time = time.time()
print(memoized_cut_rod(p, len(p)))
print("time : ",time.time() - s_time)