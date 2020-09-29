"""
N과 M (3)
https://www.acmicpc.net/problem/15651
"""
import sys

N, M = map(int, sys.stdin.readline().split())
nums = list(range(1, N+1))
answer = []


def dfs():
    if len(answer) == M:
        print(*answer)
        return
    for idx in range(N):
        answer.append(nums[idx])
        dfs()
        answer.pop()


dfs()
