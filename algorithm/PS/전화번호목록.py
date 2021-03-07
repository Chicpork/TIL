def solution(phone_book):
    answer = True
    hash_phone_book = {}
    for phone_num in phone_book:
        hash_phone_book[phone_num] = 0
    
    for phone_num in phone_book:
        temp = ""
        for number in phone_num:
            temp += number
            if temp in hash_phone_book and temp != phone_num:
                return False

    return answer