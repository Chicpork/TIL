input_num = int(input())

answer = 0

def 자릿수합(input_num):
    output_num = 0
    while input_num > 0:
        output_num += input_num % 10
        input_num = int(input_num / 10)
    
    return output_num


for i in range(1, input_num+1):
    print(자릿수합(i))
    if 자릿수합(i) + i == input_num:
        answer = i
        break

print(answer)
