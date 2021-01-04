'''
전화번호 목록
https://programmers.co.kr/learn/courses/30/lessons/42577
'''
def solution(phone_book):
    sorted_phone_book = sorted(phone_book, key= lambda x:len(x))
    pre_number = {sorted_phone_book[0]: 1}
    for index in range(1,len(phone_book)):
        for number in pre_number:
            if sorted_phone_book[index][:len(number)] in pre_number:
                return False
        pre_number[sorted_phone_book[index]] = 1
    
    return True