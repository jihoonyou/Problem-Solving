'''
피보나치
https://www.acmicpc.net/problem/9009
'''
import sys
T = int(sys.stdin.readline())
fibos = [0,1]
for i in range(2,46):
    fibos.append(fibos[-1]+fibos[-2])
for _ in range(T):
    N = int(sys.stdin.readline())
    result = []
    for i in range(45,0,-1):
        if fibos[i] <= N:
            N -= fibos[i]
            result.append(fibos[i])
        if N == 0:
            break
    print(*result[::-1])
