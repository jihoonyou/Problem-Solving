'''
N과 M (11)
https://www.acmicpc.net/problem/15665
'''
import sys

N,M = map(int,sys.stdin.readline().split())
num_in_series = sorted(map(int, sys.stdin.readline().split()))
nums = []

result = set()

def find_combinations():
    if len(nums) == M:
        result.add(tuple(nums))
        return
    for i in range(N):

        nums.append(num_in_series[i]) 
        find_combinations()
        nums.pop()


find_combinations()
result = sorted(result)

for numbers in result:
    print(*numbers)