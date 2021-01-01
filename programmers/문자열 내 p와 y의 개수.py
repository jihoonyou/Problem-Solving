'''
문자열 내 p와 y의 개수
https://programmers.co.kr/learn/courses/30/lessons/12916
'''
def solution(s):
    count = 0
    for char in s:
        if char.lower() == 'p':
            count += 1
        elif char.lower() == 'y':
            count -= 1
    return count == 0