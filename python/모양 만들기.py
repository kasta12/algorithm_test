from collections import deque

n, m = map(int, input().split())
d = []
dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]
gn = [[-1] * m for i in range(n)]
for i in range(n):
    d.append(list(map(int, input().split())))
groupSize = []
num = 0
for i in range(n):
    for j in range(m):
        if gn[i][j] == -1 and d[i][j]:
            q = deque([(i, j)])
            g = 1
            gn[i][j] = num
            while q:
                y, x = q.popleft()
                for k in range(4):
                    ny, nx = y + dy[k], x + dx[k]
                    if 0 <= ny < n and 0 <= nx < m and gn[ny][nx] == -1 and d[ny][nx]:
                        q.append((ny, nx))
                        g += 1
                        gn[ny][nx] = num
            groupSize.append(g)
            num += 1
answer = 0
for y in range(n):
    for x in range(m):
        if not d[y][x]:
            dup = set()
            val = 1
            for k in range(4):
                ny, nx = y + dy[k], x + dx[k]
                if 0 <= ny < n and 0 <= nx < m and d[ny][nx]:
                    dup.add(gn[ny][nx])
            for i in dup:
                val += groupSize[i]
            answer = max(answer, val)
print(answer)
