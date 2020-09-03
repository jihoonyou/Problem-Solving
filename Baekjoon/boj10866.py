"""
덱
https://www.acmicpc.net/problem/10866
"""
import sys
from collections import deque

N = int(sys.stdin.readline())
deq = deque()

for _ in range(N):
    cmd = sys.stdin.readline().rstrip()
    if cmd[3] == 'n':
        if len(deq):
            print(deq[0])
        else:
            print('-1')
    elif cmd[3] == 'k':
        if len(deq):
            print(deq[-1])
        else:
            print('-1')
    elif cmd[3] == 't':
        if len(deq):
            print('0')
        else:
            print('1')
    elif cmd[3] == 'e':
        print(len(deq))
    elif cmd[3] == '_':
        if cmd[4] == 'f':
            if len(deq):
                print(deq.popleft())
            else:
                print('-1')
        elif cmd[4] == 'b':
            if len(deq):
                print(deq.pop())
            else:
                print('-1')
    else:
        if cmd[5] == 'f':
            deq.appendleft(int(cmd[10:]))
        elif cmd[5] == 'b':
            deq.append(int(cmd[10:]))