n,m = input().split()

def backtracking(in_str, n, m):
    for i in range(1, int(n)+1):
        if str(i) not in in_str:
            new_in_str = in_str + str(i)
            if m == "1":
                [print(x,end=' ') for x in new_in_str]
                print()
            else:
                backtracking(new_in_str, n, str(int(m) - 1))

backtracking("", n, m)
