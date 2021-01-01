'''
같은 숫자는 싫어
https://programmers.co.kr/learn/courses/30/lessons/12906
'''
def solution(arr):
    answer = [arr[0]]
    for index in range(1,len(arr)):
        if arr[index] != answer[-1]:
            answer.append(arr[index])
    return answer