from collections import deque

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
n, l, r = map(int, input().split())
d = []
for i in range(n):
    d.append(list(map(int, input().split())))
changed = True
cnt = 0
while changed:
    changed = False
    check = [[False] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if not check[i][j]:
                check[i][j] = True
                q = deque()
                q.append([i, j])
                countries = [[i, j]]
                while q:
                    y, x = q.popleft()
                    for k in range(4):
                        ny, nx = y + dy[k], x + dx[k]
                        if 0 <= ny < n and 0 <= nx < n and not check[ny][nx]:
                            if l <= abs(d[y][x] - d[ny][nx]) <= r:
                                check[ny][nx] = True
                                q.append([ny, nx])
                                countries.append([ny, nx])
                if len(countries) > 1:
                    changed = True
                    s = 0
                    for y, x in countries:
                        s += d[y][x]
                    avg = s // len(countries)
                    for y, x in countries:
                        d[y][x] = avg
    if changed:
        cnt += 1
print(cnt)

'''
풀어봤던 문제라서 어렵지 않게 풀 수 있었음.
항상 문제를 이해하는데 시간을 쓰는 것을 아깝게 생각하면 안될 듯 하다.
'''