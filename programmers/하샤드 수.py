'''
하샤드 수
https://programmers.co.kr/learn/courses/30/lessons/12947
'''
def solution(x):
    harshad = 0
    y = x
    while y > 0:
        harshad += y % 10
        y //= 10
    if x % harshad == 0:
        return True
    return False