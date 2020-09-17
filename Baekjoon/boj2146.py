"""
다리 만들기
https://www.acmicpc.net/problem/2146
"""
import sys
from collections import deque
N = int(sys.stdin.readline())
if N == 1:
    print(0)
    exit()
country_map = []
directions = [(-1,0), (1,0), (0,-1), (0,1)]
ans = float('inf')
def grouping_island(y,x, group_num):
    queue = deque([(y,x)])
    country_map[y][x] = group_num
    while queue:
        length = len(queue)
        for _ in range(length):
            current_y, current_x = queue.popleft()
            for dir_y, dir_x in directions:
                next_y = current_y + dir_y
                next_x = current_x + dir_x
                if 0 <= next_y and next_y < N and 0 <= next_x and next_x < N and country_map[next_y][next_x] == 1:
                    queue.append((next_y,next_x))
                    country_map[next_y][next_x] = group_num

def make_bridge(group):
    global ans
    dist = [ [-1 for _ in range(N)]for _ in range(N) ]
    q = deque()
    for y in range(N):
        for x in range(N):
            if country_map[y][x] == group:
                q.append((y,x))
                dist[y][x] = 0
    while q:
        curr_y, curr_x = q.popleft()
        for dir_y, dir_x in directions:
            next_y = curr_y + dir_y
            next_x = curr_x + dir_x
            if 0 <= next_y and next_y < N and 0 <= next_x and next_x < N:
                if country_map[next_y][next_x] and country_map[next_y][next_x] != group:
                    ans = min(ans, dist[curr_y][curr_x])
                    return
                if not country_map[next_y][next_x] and dist[next_y][next_x] == -1:
                    q.append((next_y,next_x))
                    dist[next_y][next_x] = dist[curr_y][curr_x] + 1
for _ in range(N):
    country_map.append(list(map(int,sys.stdin.readline().split())))
group_num = 2
for y in range(N):
    for x in range(N):
        if country_map[y][x] == 1:
            grouping_island(y,x, group_num)
            group_num += 1

for group in range(2,group_num):
    make_bridge(group)

print(ans)
# boundary를 따로 구해서 queue에 넣으면 더 빠를 수 있을듯.. 