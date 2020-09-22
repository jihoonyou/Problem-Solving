"""
줄세우기
https://www.acmicpc.net/problem/2252
"""
import sys
from collections import deque
N,M = map(int,sys.stdin.readline().split())

adj_list = [[] for _ in range(N+1)]
in_degree = {i:0 for i in range(1,N+1)}
row = []

for _ in range(M):
    small_student, big_student = map(int,sys.stdin.readline().split())
    adj_list[small_student].append(big_student)
    in_degree[big_student] += 1

sources = deque()

for student in in_degree:
    if in_degree[student] == 0:
        sources.append(student)

while sources:
    student = sources.popleft()
    row.append(str(student))

    for taller_student in adj_list[student]:
        in_degree[taller_student] -= 1
        if in_degree[taller_student] == 0:
            sources.append(taller_student)

print(' '.join(row))
