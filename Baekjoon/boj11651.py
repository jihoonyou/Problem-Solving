"""
좌표 정렬하기 2
https://www.acmicpc.net/problem/11651
"""
N = int(input())
nums = []

for _ in range(N):
    temp = input().split()
    nums.append((int(temp[0]),int(temp[1])))

sorted_nums = sorted(nums, key=lambda x: (x[1],x[0]))

for num in sorted_nums:
    print(num[0],num[1])
    