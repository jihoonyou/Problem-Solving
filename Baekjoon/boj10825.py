"""
국영수
https://www.acmicpc.net/problem/10825
"""
import sys
N = int(sys.stdin.readline())
student_info = []
for _ in range(N):
    [name, kor, eng, math] = sys.stdin.readline().split()
    student_info.append((name,int(kor),int(eng),int(math)))

sorted_info = sorted(student_info, key=lambda x: (-x[1], x[2], -x[3], x[0]))

for info in sorted_info:
    print(info[0])