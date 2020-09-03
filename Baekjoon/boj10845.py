"""
큐
https://www.acmicpc.net/problem/10845
"""
import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque([])

for _ in range(N):
    cmd = sys.stdin.readline().rstrip()
    if cmd[1] == 'u':
        queue.append(cmd[5:])
    elif cmd[1] == 'o':
        if len(queue):
            element = queue.popleft()
            print(element)
        else:
            print('-1')
    elif cmd[1] == 'i':
        print(len(queue))
    elif cmd[1] == 'm':
        if len(queue):
            print('0')
        else:
            print('1')
    elif cmd[1] == 'r':
        if len(queue):
            print(queue[0])
        else:
            print('-1')
    else:
        if len(queue):
            print(queue[-1])
        else:
            print('-1')