'''
두 정수 사이의 합
https://programmers.co.kr/learn/courses/30/lessons/12912
'''
def solution(a, b):
    if a > b:
        return sum(range(b,a+1))
    return sum(range(a,b+1))