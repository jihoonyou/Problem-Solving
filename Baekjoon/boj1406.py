"""
에디터
https://www.acmicpc.net/problem/1406
"""
import sys
from collections import deque

left_stack = list(sys.stdin.readline().strip())
right_stack = deque()
N = int(sys.stdin.readline())

for _ in range(N):
    cmd = sys.stdin.readline()
    if cmd[0] == 'L':
        if len(left_stack): 
            right_stack.appendleft(left_stack.pop())
    elif cmd[0] == 'D':
        if len(right_stack):
            left_stack.append(right_stack.popleft())
    elif cmd[0] == 'B':
        if len(left_stack):
            left_stack.pop()
    else:
        left_stack.append(cmd[2])

print(''.join(left_stack+list(right_stack)))