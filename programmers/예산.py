'''
예산
https://programmers.co.kr/learn/courses/30/lessons/12982
'''
def solution(d, budget):
    answer = 0
    d.sort()
    for money in d:
        if budget >= money:
            budget -= money
            answer += 1
        else:
            break
    return answer