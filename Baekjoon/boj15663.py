'''
N과 M (9)
https://www.acmicpc.net/problem/boj15663
'''
import sys

N,M = map(int,sys.stdin.readline().split())
num_in_series = sorted(map(int, sys.stdin.readline().split()))
nums = []
visited = [False]*N
result = set()

def find_combinations():
    if len(nums) == M:
        # print(*nums)
        result.add(tuple(nums))
        return
    for i in range(N):
        if visited[i]:
            continue
        visited[i] = True
        nums.append(num_in_series[i]) 
        find_combinations()
        nums.pop()
        visited[i] = False


find_combinations()
result = sorted(result)

for numbers in result:
    print(*numbers)