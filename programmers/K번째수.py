'''
K번째수
https://programmers.co.kr/learn/courses/30/lessons/42748?language=python3
'''
def solution(array, commands):
    answer = []
    for command in commands:
        _array = sorted(array[command[0]-1:command[1]])
        answer.append(_array[command[2]-1])
    return answer