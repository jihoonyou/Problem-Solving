"""
좌표 정렬하기
https://www.acmicpc.net/problem/11650
"""
N = int(input())
nums = []

for _ in range(N):
    temp = input().split()
    nums.append((int(temp[0]),int(temp[1])))

sorted_nums = sorted(nums, key=lambda x: (x[0],x[1]))

for num in sorted_nums:
    print(num[0],num[1])
    