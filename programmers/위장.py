'''
위장
https://programmers.co.kr/learn/courses/30/lessons/42578
'''
def solution(clothes):
    answer = 1
    types = {}
    for element in clothes:
        if element[1] not in types:
            types[element[1]]  = []
        types[element[1]].append(element[0])
    for value in types:
        answer *= (len(types[value])+1)
    return answer-1
    