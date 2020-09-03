"""
수 정렬하기 3
https://www.acmicpc.net/problem/10989
"""
import sys
MAX_NUM = 10001
N = int(sys.stdin.readline())
nums = [0]*MAX_NUM

for _ in range(N):
    nums[int(sys.stdin.readline())]+=1

for i in range(1,MAX_NUM):
    if nums[i] !=0:
        for _ in range(nums[i]):
            print(i)