'''
124 나라의 숫자
https://programmers.co.kr/learn/courses/30/lessons/12899
'''
def solution(n):
    answer = ''
    while n > 0:
        n, mod = divmod(n,3)
        answer = '412'[mod] + answer
        if mod == 0:
            n -= 1 
    return answer
    # answer = ''
    # while n > 0:
    #     answer = '412'[n%3] + answer
    #     if n % 3 == 0:
    #         n -= 1
    #     n //= 3    
    # return answer