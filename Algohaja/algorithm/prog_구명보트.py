def solution(people, limit):
    people.sort(reverse=True)
    
    answer = 0
    lower_limit = limit - 40
    people_pop = [0]*len(people)

    for ix in range(0, len(people)-1):
        if people[ix] > lower_limit:
            people_pop[ix] = 1
        else:
            break

    max_idx = len(people)-1
    for ix, person1 in enumerate(people):
        if people_pop[ix] == 0:
            if ix >= max_idx:
                people_pop[ix] = 1
                break
        
            if person1 + people[max_idx] <= limit:
                people_pop[ix] = 0.5
                people_pop[max_idx] = 0.5
                max_idx -= 1
            else:
                people_pop[ix] = 1

    return answer + int(sum(people_pop))