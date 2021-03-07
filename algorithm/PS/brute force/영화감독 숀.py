series = int(input())

num = 0
while series > 0:
    num += 1
    if str(num).find("666") >= 0:
        series -= 1    

print(num)
