'''
절댓값 힙
https://www.acmicpc.net/problem/11286
'''
import sys
import heapq

N = int(sys.stdin.readline())
heap = []

while N:
    x = int(sys.stdin.readline())
    if not x:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap,(abs(x),x))
    N-=1