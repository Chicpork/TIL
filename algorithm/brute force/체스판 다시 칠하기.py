m ,n = [int(x) for x in input().split(' ')]

check_chess = []

for i in range(0, m):
    check_chess.append(input())

def 정답(chess):
    num1 = 0
    num2 = 0

    for i, item in enumerate(chess):
        for j, item2 in enumerate(item):
            if (i+j)%2==0 and item2 == 'W':
                num1 += 1
            elif (i+j)%2==1 and item2 == 'B':
                num1 += 1
            
            if (i+j)%2==0 and item2 == 'B':
                num2 += 1
            elif (i+j)%2==1 and item2 == 'W':
                num2 += 1
    return min(64 - num1, 64 - num2)

anwser = m*n
for i in range(m-7):
    for j in range(n-7):
        if anwser > 정답([x[j:j+8] for x in check_chess[i:i+8]]):
            anwser = 정답([x[j:j+8] for x in check_chess[i:i+8]])

print(anwser)
