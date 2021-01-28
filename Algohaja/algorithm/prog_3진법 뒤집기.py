def solution(n):
    digit = []
    while True:
        if n < 3:
            digit.append(n)
            break
        digit.append(n%3)
        n = int(n/3)
        
    return sum([di*pow(3,len(digit)-ix-1) for ix, di in enumerate(digit)])