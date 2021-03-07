def solution(progresses, speeds):
    answer = []

    while True:
        progresses = [a + b for a, b in zip(progresses, speeds)]
        pop_cnt = 0
        while True:
            if len(progresses) <= 0:
                break

            if progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                pop_cnt += 1
            else:
                break
        
        if pop_cnt > 0:
            answer.append(pop_cnt)
                
        if len(progresses) <= 0:
            break

    return answer

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]	))
