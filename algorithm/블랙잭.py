card_number, max_number = [int(x) for x in input().split(' ')]
input_numbers = [int(x) for x in input().split(' ')]

max_output = 0

for i in range(0,card_number):
    for j in range(1+i,card_number):
        for k in range(1+j,card_number):
            temp_sum = input_numbers[i] + input_numbers[j] + input_numbers[k]
            if temp_sum > max_output and temp_sum <= max_number:
                max_output = temp_sum

print(max_output)