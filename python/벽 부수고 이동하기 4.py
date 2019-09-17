from _collections import deque

dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]
n, m = map(int, input().split())
d = []
for i in range(n):
    d.append(list(map(int, list(input()))))
dist = [[0] * m for i in range(n)]
gn = [[-1] * m for i in range(n)]
check = [[False] * m for i in range(n)]
group = []
for i in range(n):
    for j in range(m):
        if not d[i][j] and not check[i][j]:
            q = deque()
            g = []
            q.append((i, j))
            g.append([i, j])
            check[i][j] = True
            while q:
                y, x = q.popleft()
                for k in range(4):
                    ny, nx = y + dy[k], x + dx[k]
                    if 0 <= ny < n and 0 <= nx < m and not d[ny][nx] and not check[ny][nx]:
                        q.append((ny, nx))
                        g.append([ny, nx])
                        check[ny][nx] = True
            group.append(g)
idx = 0
for g in group:
    for y, x in g:
        dist[y][x] = len(g)
        gn[y][x] = idx
    idx += 1

for i in range(n):
    for j in range(m):
        val = 0
        if d[i][j] == 1:
            val += 1
            dup = []
            for k in range(4):
                ny, nx = i + dy[k], j + dx[k]
                if 0 <= ny < n and 0 <= nx < m and gn[ny][nx] not in dup:
                    dup.append(gn[ny][nx])
                    val += dist[ny][nx]
        print(val % 10, end="")
    print()
