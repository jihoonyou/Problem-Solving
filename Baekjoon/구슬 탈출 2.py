'''
구슬 탈출 2
https://www.acmicpc.net/problem/13460
'''
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int,input().split())
maze = [ [0 for _ in range(M)] for _ in range(N) ]
move = [(0,1),(1,0),(0,-1),(-1,0)] # down right up left
visited = {}
queue = deque()

def init():
    blue = None
    red = None
    for i in range(N):
        line = input()
        for j in range(M):
            maze[i][j] = line[j]
            if line[j] == 'R': 
                red = [i,j]
                maze[i][j] = '.'
            elif line[j] == 'B':
                blue = [i,j]
                maze[i][j] = '.'
    queue.append((red[0],red[1],blue[0],blue[1],1))
    visited[(red[0],red[1],blue[0],blue[1])] = True

def moves(cur_r, cur_c, m_r, m_c):
    count = 0 
    while maze[cur_r][cur_c] != 'O' and maze[cur_r + m_r][cur_c + m_c] != '#':
        cur_r += m_r
        cur_c += m_c
        count += 1
    return cur_r, cur_c, count

def bfs(q):
    while q:
        cur_red_r, cur_red_c, cur_blue_r, cur_blue_c, count = q.popleft()
        if count > 10:
            break
        for m_r,m_c in move:
            next_red_r, next_red_c, r_count = moves(cur_red_r,cur_red_c, m_r, m_c)
            next_blue_r, next_blue_c, b_count = moves(cur_blue_r,cur_blue_c, m_r, m_c)

            # blue 먼저 들어갔는지 확인
            if maze[next_blue_r][next_blue_c] == 'O':
                continue
            if maze[next_red_r][next_red_c] == 'O':
                print(count)
                return
            # red와 blue가 동시에 같은 칸 일 때
            if next_red_r == next_blue_r and next_blue_c == next_red_c:
                if r_count < b_count:
                    next_blue_r -= m_r
                    next_blue_c -= m_c
                else:
                    next_red_r -= m_r
                    next_red_c -= m_c
            if (next_red_r, next_red_c, next_blue_r, next_blue_c) not in visited:
                visited[(next_red_r, next_red_c, next_blue_r, next_blue_c)] = True
                q.append((next_red_r, next_red_c, next_blue_r, next_blue_c, count+1))
    print(-1)
def main():
    init()
    bfs(queue)
main()