"""
N과 M (4)
https://www.acmicpc.net/problem/15652
"""
import sys

N, M = map(int, sys.stdin.readline().split())
nums = range(1, N+1)
answer = []


def dfs(start):
    if len(answer) == M:
        print(*answer)
        return

    for index in range(start, N):
        answer.append(nums[index])
        dfs(index)
        answer.pop()


dfs(0)
