import copy

n, m = map(int, input().split())
d = []
for i in range(n):
    d.append(list(input()))
fd = copy.deepcopy(d)
k = (min(n, m) - 1) // 2
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
result = []
for y in range(n):
    for x in range(m):
        if d[y][x] == "*":
            for i in range(k, 0, -1):  # 십자가 크기
                ok = True
                if y + i < n and y - i >= 0 and x + i < m and x - i >= 0:
                    for j in range(4):
                        ny = y
                        nx = x
                        for _ in range(i):
                            ny += dy[j]
                            nx += dx[j]
                            if d[ny][nx] != "*":
                                ok = False
                else:
                    ok = False
                if ok:
                    fd[y][x] = "."
                    for j in range(4):
                        ny = y
                        nx = x
                        for _ in range(i):
                            ny += dy[j]
                            nx += dx[j]
                            fd[ny][nx] = "."
                    result.append([y + 1, x + 1, i])
                    break
for i in range(n):
    for j in range(m):
        if fd[i][j] == "*":
            print(-1)
            exit()
print(len(result))
for i in result:
    print(" ".join(map(str, i)))
