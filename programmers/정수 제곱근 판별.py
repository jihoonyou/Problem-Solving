'''
정수 제곱근 판별
https://programmers.co.kr/learn/courses/30/lessons/12934
'''
def solution(n):
    sqrt = n**0.5
    if sqrt == int(sqrt):
        return (sqrt+1)**2
    return -1