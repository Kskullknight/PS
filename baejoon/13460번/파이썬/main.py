# 최단 거리로 이동하는 방법을 구한 다음
# 각 최단 거리중에서 통과할 수 있는 경로가 있는지 확인

import queue

N, M = map(int, input().split())

board = list()

for i in range(N):
    line = list(map(int, input().split()))
    if line in 'R':
        ry = i
        rx = line.find('R')
    if line in 'B':
        by = i
        bx = line.find('B')
    
direction_x = [1, -1, 0, 0]
direction_y = [0, 0, 1, -1]

def move_end(vis, cur):
    count = 0
    while True:
        next_cur_x = cur[0] + direction_x[i]
        next_cur_y = cur[0] + direction_y[i]
        if vis[next_cur_x][next_cur_y] == '#' or vis[next_cur_x][next_cur_y] == '0':
            break
        count += 1
    return count

vis = [[0] * M for i in range(N)]

q = queue.Queue()

queue.put((rx, ry))
queue.put((bx, by))

vis[x][y] = 1

while queue.empty():
    cur = q.get()
    for i in range(len(direction_x)):
        count = move_end
        if count != 0:
            queue.put((cur[0] + direction_x[i] * count, cur[1] + direction_y[i] * count))

