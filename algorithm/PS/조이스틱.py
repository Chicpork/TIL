def solution(name):
    name_num = []
    name_complete = [0]*len(name)
    name_complete_num = 0
    for char in name:
        name_num.append((ord(char) - 65, (ord(char)-91)*-1))
    
    print(name_num)
    print(name_complete)

    idx = 0
    while (name_complete_num == len(name)):
        if name_num[idx][0] == 0 or name_num[idx][1] == 0:
            name_complete_num += 1
        
        


    return 0

print(ord("A"))
print(ord("Z"))
print(solution("ABXZ"))
