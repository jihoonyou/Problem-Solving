'''
프린터
https://programmers.co.kr/learn/courses/30/lessons/42587
'''
from collections import deque
def solution(priorities, location):
    answer = 0
    queue = deque([(v,i) for i,v in enumerate(priorities)])
    _priorities = deque(sorted(priorities, reverse=True))
    
    while deque:
        curr = queue.popleft()
        if curr[0] == _priorities[0]:
            answer += 1
            _priorities.popleft()
            if curr[1] == location:
                return answer
        else:
            queue.append(curr)
        