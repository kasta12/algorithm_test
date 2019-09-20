from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
n = int(input())
d = [list(input()) for _ in range(n)]
dist = [[-1] * n for _ in range(n)]
m = [[list() for _ in range(n)] for __ in range(n)]
door_mirror = []
start, end = (), ()

for i in range(n):
    for j in range(n):
        if d[i][j] == "!":
            door_mirror.append((i, j))
        if d[i][j] == "#":
            door_mirror.append((i, j))
            if not start:
                start = (i, j)
            else:
                end = (i, j)
for y, x in door_mirror:
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        while 0 <= ny < n and 0 <= nx < n:
            if d[ny][nx] == "*":
                break
            if d[ny][nx] == "#" or d[ny][nx] == "!":
                m[y][x].append((ny, nx))
            ny += dy[k]
            nx += dx[k]

q = deque()
q.append(start)
dist[start[0]][start[1]] = 0
while q:
    y, x = q.popleft()
    for ny, nx in m[y][x]:
        if dist[ny][nx] == -1:
            dist[ny][nx] = dist[y][x] + 1
            q.append((ny, nx))
print(dist[end[0]][end[1]] - 1)
