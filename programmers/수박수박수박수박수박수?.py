'''
수박수박수박수박수박수?
https://programmers.co.kr/learn/courses/30/lessons/12922
'''
def solution(n):
    answer = ''
    for i in range(n):
        if i % 2:
            answer += '박'
        else:
            answer += '수'
    return answer