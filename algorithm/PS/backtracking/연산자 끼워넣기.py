import sys
import copy

N = int(sys.stdin.readline())

numbers = list(map(int, sys.stdin.readline().rstrip().split()))
operators = list(map(int, sys.stdin.readline().rstrip().split()))

operation_list = []

def insertOperation(arr_in):
    for operation in operation_list:
        if operation == arr_in:
            return
    
    operation_list.append(copy.deepcopy(arr_in))

def getOperations(arr_in):
    if len(arr_in) == N-1:
        # insertOperation(arr_in)
        operation_list.append(copy.deepcopy(arr_in))
        return
    
    for i in range(4):
        if operators[i] != 0:
            operators[i] -= 1
            arr_in.append(i)
            getOperations(arr_in)
            arr_in.pop()
            operators[i] += 1

getOperations([])

# print(operation_list)

max_output = -1000000000
min_output = 1000000000
for operation in operation_list:
    output = numbers[0]
    for i, operator in enumerate(operation):
        if operator == 0:
            output += numbers[i+1]
        elif operator == 1:
            output -= numbers[i+1]
        elif operator == 2:
            output *= numbers[i+1]
        else:
            if output < 0:
                output *= -1
                output //= numbers[i+1]
                output *= -1
            else:
                output //= numbers[i+1]

    if max_output < output:
        # print("max",operation, output)
        max_output = output
    
    if min_output > output:
        # print("min",operation, output)
        min_output = output

print(max_output)
print(min_output)
