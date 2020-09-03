"""
괄호
https://www.acmicpc.net/problem/9012
"""
import sys

N = int(sys.stdin.readline())

for _ in range(N):
    counter = 0
    parentheses = sys.stdin.readline().rstrip()

    for parenthesis in parentheses:
        if parenthesis == '(':
            counter += 1
        else:
            counter -= 1
            if counter < 0:
                break
    if counter == 0:
        print('YES')
    else:
        print('NO')
    