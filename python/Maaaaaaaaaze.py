from copy import deepcopy
from collections import deque

dc = deepcopy
d = []
m1, m2, m3, m4, m5 = [], [], [], [], []
for j in range(5):
    m1.append(list(map(int, input().split())))
for j in range(5):
    m2.append(list(map(int, input().split())))
for j in range(5):
    m3.append(list(map(int, input().split())))
for j in range(5):
    m4.append(list(map(int, input().split())))
for j in range(5):
    m5.append(list(map(int, input().split())))


def rotate(mat, num):
    for n in range(num):
        temp = dc(mat)
        for i in range(5):
            for j in range(5):
                mat[j][i] = temp[i][4 - j]


dz = [1, 0, 0, -1, 0, 0]
dy = [0, 1, 0, 0, -1, 0]
dx = [0, 0, 1, 0, 0, -1]
answer = 9999999999999


def bfs(z, y, x, cnt):
    if d[0][0][0] == 0:
        return -1
    dist = [[[-1] * 5 for j in range(5)] for i in range(5)]
    q = deque()
    q.append((0, 0, 0))
    dist[0][0][0] = 0
    while q:
        x, y, z = q.popleft()
        for k in range(6):
            nx, ny, nz = x + dx[k], y + dy[k], z + dz[k]
            if 0 <= nx < 5 and 0 <= ny < 5 and 0 <= nz < 5:
                if d[nx][ny][nz] == 1 and dist[nx][ny][nz] == -1:
                    dist[nx][ny][nz] = dist[x][y][z] + 1
                    q.append((nx, ny, nz))
    return dist[4][4][4]


for i in range(4):
    rotate(m1, 1)
    for j in range(4):
        rotate(m2, 1)
        for k in range(4):
            rotate(m3, 1)
            for l in range(4):
                rotate(m4, 1)
                for m in range(4):
                    rotate(m5, 1)
                    for a in range(5):
                        for b in range(5):
                            for c in range(5):
                                for e in range(5):
                                    for f in range(5):
                                        temp = [a, b, c, e, f]
                                        if 0 in temp and 1 in temp and 2 in temp and 3 in temp and 4 in temp:
                                            for g in temp:
                                                if g == 0:
                                                    d.append(m1)
                                                elif g == 1:
                                                    d.append(m2)
                                                elif g == 2:
                                                    d.append(m3)
                                                elif g == 3:
                                                    d.append(m4)
                                                elif g == 4:
                                                    d.append(m5)
                                            check = [[[False] * 5 for n in range(5)] for o in range(5)]
                                            if d[0][0][0]:
                                                check[0][0][0] = True
                                                cur = bfs(0, 0, 0, 0)
                                                if cur != -1:
                                                    answer = min(answer, cur)
                                            d.clear()

if answer == 9999999999999:
    print(-1)
else:
    print(answer)
