people = int(input())
lists = []
for i in range(people):
    lists.append(input().split(' '))

for j in range(0, len(lists)):
    number = 1
    for i in range(0, len(lists)):
        if i != j:
            if lists[j][0] < lists[i][0] and lists[j][1] < lists[i][1]:
                number += 1
    
    print(str(number) + ' ',end="")