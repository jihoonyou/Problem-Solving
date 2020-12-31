'''
이상한 문자 만들기
https://programmers.co.kr/learn/courses/30/lessons/12930
'''
def solution(s):
    answer = ''
    reset = 0
    for char in s:
        if ord(char) == 32:
            answer += ' '
            reset = 0
        elif reset % 2 == 0:
            answer += char.upper()
            reset += 1
        else:
            answer += char.lower()
            reset += 1
    return answer