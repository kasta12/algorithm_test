n, m = map(int, input().split(" "))
d = []
for i in range(n):
    d.append(list(map(int, input().split(" "))))
check = [[False] * 500 for i in range(500)]

ys = []
xs = []
dy = [0, 0, 1]
dx = [1, -1, 0]
answer = -1


def dfs(y, x, cnt):
    global answer
    ys.append(y)
    xs.append(x)
    check[y][x] = True
    if cnt == 3:
        temp = 0
        for i in range(4):
            temp += d[ys[i]][xs[i]]
            answer = max(temp, answer)
    else:
        for i in range(3):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and not check[ny][nx]:
                dfs(ny, nx, cnt + 1)
    ys.pop()
    xs.pop()
    check[y][x] = False


for y in range(n):
    for x in range(m):
        dfs(y, x, 0)
        if y + 2 < n:
            temp = d[y][x] + d[y + 1][x] + d[y + 2][x]
            if x + 1 < m:
                temp += d[y + 1][x + 1]
                answer = max(temp, answer)
                temp -= d[y + 1][x + 1]
            if x - 1 >= 0:
                temp += d[y + 1][x - 1]
                answer = max(temp, answer)
                temp -= d[y + 1][x - 1]
        if x + 2 < m:
            temp = d[y][x] + d[y][x + 1] + d[y][x + 2]
            if y + 1 < n:
                temp += d[y + 1][x + 1]
                answer = max(temp, answer)
                temp -= d[y + 1][x + 1]
            if y - 1 >= 0:
                temp += d[y - 1][x + 1]
                answer = max(temp, answer)
                temp -= d[y - 1][x + 1]

print(answer)

'''
전형적인 Brute Force 문제. 하지만 더 효과적으로 해결하는 방법을 찾는 것이 중요한 문제였다.
그냥 케이스 분리해서 풀면 코드 쓰는데 엄청난 시간이 걸리는 문제이다.
'''