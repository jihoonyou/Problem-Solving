'''
N과 M (12)
https://www.acmicpc.net/problem/15666
'''
import sys

N,M = map(int,sys.stdin.readline().split())
num_in_series = sorted(map(int, sys.stdin.readline().split()))
nums = []
visited = [False]*N
result = set()

def find_combinations(start):
    if len(nums) == M:
        result.add(tuple(nums))
        return
    for i in range(start, N):
        if len(nums) and nums[-1] > num_in_series[i]:
            continue
        nums.append(num_in_series[i]) 
        find_combinations(i)
        nums.pop()



find_combinations(0)
result = sorted(result)

for numbers in result:
    print(*numbers)