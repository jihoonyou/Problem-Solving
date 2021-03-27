'''
최대 힙
https://www.acmicpc.net/problem/11279
'''
import sys
import heapq

N = int(sys.stdin.readline())
heap = []
while N:
    x = int(sys.stdin.readline())

    if x > 0:
        heapq.heappush(heap, -x)
    else:
        if not heap:
            print(0)
        else:
            print(abs(heapq.heappop(heap)))
    N -= 1
