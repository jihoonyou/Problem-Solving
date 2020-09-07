"""
소수 찾기
https://www.acmicpc.net/problem/1978
"""
import sys

MAX_N = 1000
prime_arr = [False,False] + [True]*(MAX_N-1)

for i in range(2,MAX_N+1):
    if prime_arr[i]:
        for j in range(2*i,MAX_N+1, i):
            prime_arr[j] = False

N = sys.stdin.readline()
prime_nums = list(map(int,sys.stdin.readline().split()))
res = 0
for num in prime_nums:
    if prime_arr[num] == True:
        res += 1
print(res)