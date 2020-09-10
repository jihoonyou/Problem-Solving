"""
텀 프로젝트
https://www.acmicpc.net/problem/9466
"""
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    students = [0] + list(map(int, sys.stdin.readline().split()))
    team = [0]*(N+1)

    for i in range(1, N+1):
        if team[i] == 0:
            team_number = i
            while team[i] == 0:
                team[i] = team_number
                i = students[i]
            while team[i] == team_number:
                team[i] = -1
                i = students[i]
    print(N - team.count(-1))
