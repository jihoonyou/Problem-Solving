'''
x만큼 간격이 있는 n개의 숫자
https://programmers.co.kr/learn/courses/30/lessons/12954
'''
def solution(x, n):
    answer = []
    start = 0
    while n != 0:
        start += x
        answer.append(start)
        n -= 1
    return answer