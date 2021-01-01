'''
3진법 뒤집기
https://programmers.co.kr/learn/courses/30/lessons/68935
'''
def reverse_convert(num):
    converted_n = ''
    while num != 0:
        converted_n += str(num % 3) 
        num //= 3
    return converted_n
def solution(n):
    num = int(reverse_convert(n))
    answer = 0
    count = 0
    
    while num != 0:
        temp = num % 10
        num //= 10
        answer += temp * (3**count)
        count += 1
    
    return answer