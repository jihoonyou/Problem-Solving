'''
N-Queen
https://www.acmicpc.net/problem/9663
'''
import sys

N = int(sys.stdin.readline())

result = [0]
row = [0]*N

def is_valid(index):
    for i in range(index):
        diff = abs(row[index]-row[i])
        if diff == 0 or diff == index - i:
            return False
    return True

def find_n_queens(x):
    if x == N:
        result[0] += 1
    else:
        for i in range(N):
            row[x] = i
            if is_valid(x):
                find_n_queens(x+1)
find_n_queens(0)
print(result[0])

