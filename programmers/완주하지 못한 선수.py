'''
완주하지 못한 선수
https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3
'''
def solution(participant, completion):
    comp_dict = dict()
    for player in completion:
        if player not in comp_dict:
            comp_dict[player] = 1
        else:
            comp_dict[player] += 1
    for player in participant:    
        if player not in comp_dict:
            return player
        else:
            comp_dict[player] -= 1
            if comp_dict[player] == 0:
                del comp_dict[player]