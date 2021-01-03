'''
더 맵게
https://programmers.co.kr/learn/courses/30/lessons/42626
'''
import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) != 1 and scoville[0] < K:
        food1 = heapq.heappop(scoville)
        food2 = heapq.heappop(scoville)
        new_scoville = food1 + food2*2
        heapq.heappush(scoville,new_scoville)
        answer += 1
    return answer if scoville[0] >= K else -1