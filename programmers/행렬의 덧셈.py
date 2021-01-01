'''
행렬의 덧셈
https://programmers.co.kr/learn/courses/30/lessons/12950
'''
def solution(arr1, arr2):
    answer = []
    index = 0
    for x,y in zip(arr1, arr2):
        answer.append([])
        for i in range(len(x)):
            answer[index].append(x[i]+y[i])
        index += 1
    return answer