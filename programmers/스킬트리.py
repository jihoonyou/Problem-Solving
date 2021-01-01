'''
스킬트리
https://programmers.co.kr/learn/courses/30/lessons/49993
'''
def solution(skill, skill_trees):
    answer = 0
    for s in skill_trees:
        learned = 0
        finished = True
        for spell in s:
            if spell in skill:
                if spell == skill[learned]:
                    learned += 1
                else:
                    finished = False
                    break
        if finished:
            answer += 1
    return answer