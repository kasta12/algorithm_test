from copy import deepcopy

n, m, d = map(int, input().split())
archer = []
castle = []
for i in range(n):
    castle.append(list(map(int, input().split())))
answer = 0


def dfs(idx, cur):
    global answer
    if cur == 3:
        temp = deepcopy(castle)
        maxVal = 0
        for _ in range(n):
            rem = []
            for i in archer:
                result = (n, m, d)
                py, px = n, i
                for y in range(n):
                    for x in range(m):
                        if temp[y][x]:
                            dist = abs(py - y) + abs(px - x)
                            if dist < result[2] or (dist == result[2] and x < result[1]):
                                result = (y, x, dist)
                if result[0] != n and result[1] != m:
                    rem.append((result[0], result[1]))
            for y, x in rem:
                if temp[y][x]:
                    temp[y][x] = 0
                    maxVal += 1
            for i in range(n - 1, -1, -1):
                for j in range(m):
                    if i == 0:
                        temp[i][j] = 0
                    else:
                        temp[i][j] = temp[i - 1][j]
        answer = max(answer, maxVal)
    elif idx == m:
        return
    else:
        archer.append(idx)
        dfs(idx + 1, cur + 1)
        archer.pop()
        dfs(idx + 1, cur)


dfs(0, 0)
print(answer)
