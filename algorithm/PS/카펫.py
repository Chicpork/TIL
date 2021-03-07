def solution(brown, yellow):
    answer = []

    for x in range(1, (yellow+1)//2+1):
        if yellow%x == 0:
            brown_x = x+2
            brown_y = yellow//x+2
            if brown_x*brown_y - yellow == brown:
                answer = [brown_y, brown_x]
                break

    return answer

print(solution(10, 2))


