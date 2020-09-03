"""
나이순 정렬
https://www.acmicpc.net/problem/10814
"""
import sys

N = int(sys.stdin.readline())
user_list = []

for _ in range(N):
    temp = sys.stdin.readline().split()
    user_list.append((int(temp[0]),temp[1]))

sorted_user_list = sorted(user_list, key=lambda x: x[0])

for user_info in sorted_user_list:
    print(user_info[0],user_info[1])