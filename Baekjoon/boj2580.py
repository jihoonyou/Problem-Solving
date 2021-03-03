'''
스도쿠
https://www.acmicpc.net/problem/2580
'''
import sys

sudoku = [list(map(int,sys.stdin.readline().split())) for _ in range(9)]
zeros = [(i,j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]
is_complete = [False]

def check_horizontal(x,val):
    if val in sudoku[x]:
        return False
    return True

def check_vertical(y, val):
    for index in range(9):
        if val == sudoku[index][y]:
            return False
    return True

def check_sqaure(x,y,val):
    _x = x//3 * 3
    _y = y//3 * 3

    for i in range(3):
        for j in range(3):
            if val == sudoku[_x+i][_y+j]:
                return False
    return True

def solve(x):
    if is_complete[0]:
        return
    if len(zeros) == x:
        for row in sudoku:
            for val in row:
                print(val, end=' ')
            print()
        is_complete[0] = True
    else:
        for i in range(1,10):
            nx = zeros[x][0]
            ny = zeros[x][1]
            if check_horizontal(nx, i) and check_vertical(ny, i) and check_sqaure(nx,ny, i):
                sudoku[nx][ny] = i
                solve(x+1)
                sudoku[nx][ny] = 0
solve(0)