"""
스택
https://www.acmicpc.net/problem/10828
"""
import sys

N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    command = sys.stdin.readline()
    if command[:2] == 'pu':
        stack.append(int(command[5:]))
    elif command[:2] == 'po':
        if len(stack):
            print(stack[-1])
            stack.pop()
        else:
            print('-1')
    elif command[:2] == 'si':
        print(len(stack))
    elif command[:2] == 'em':
        if len(stack):
            print('0')
        else:
            print('1')
    else:
        if len(stack):
            print(stack[-1])
        else:
            print('-1')
