import sys

N = int(sys.stdin.readline())

for _ in range(N):
    (x,y) = map(int, sys.stdin.readline().rstrip().split())
    distance = y-x
    n = int(distance ** 0.5)
    n2 = n**2
    if n2 == distance:
        print(2*n - 1)
    elif distance > n2 and distance <= n2 + n:
        print(2*n)
    elif distance > n2 + n and distance <= (n+1)**2:
        print(2*(n+1) - 1)
