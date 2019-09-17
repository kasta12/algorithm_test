from collections import deque
import sys
sys.setrecursionlimit(1000000)
n, m = map(int, input().split())
d = []
dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]
for i in range(n):
    d.append(list(map(int, input().split())))
answer = 0


def ok(y, x):
    for k in range(4):
        ny, nx = y + dy[k], x + dx[k]
        if 0 <= ny < n and 0 <= nx < m and d[ny][nx] == 2:
            return True
    return False


def dfs(y, x, cnt):
    global answer
    if cnt == 2 or y == n:
        check = [[False] * m for i in range(n)]
        val = 0
        for i in range(n):
            for j in range(m):
                if d[i][j] == 2 and not check[i][j]:
                    q = deque()
                    q.append((i, j))
                    check[i][j] = True
                    valid = True
                    cnt = 1
                    while q:
                        a, b = q.popleft()
                        for k in range(4):
                            ny, nx = a + dy[k], b + dx[k]
                            if 0 <= ny < n and 0 <= nx < m and not check[ny][nx]:
                                if d[ny][nx] == 2:
                                    check[ny][nx] = True
                                    q.append((ny, nx))
                                    cnt += 1
                                elif d[ny][nx] == 0:
                                    valid = False
                    if valid:
                        val += cnt
        answer = max(val, answer)

    elif x == m:
        dfs(y + 1, 0, cnt)
    elif not d[y][x] and ok(y, x):
        d[y][x] = 1
        dfs(y, x + 1, cnt + 1)
        d[y][x] = 0
        dfs(y, x + 1, cnt)
    else:
        dfs(y, x + 1, cnt)


dfs(0, 0, 0)
print(answer)

'''
Hard문제의 경우 코딩테스트에 나오지 않을 수준이므로 pass
DFS, BFS를 섞어서 풀었음. 하지만 반복문므로 DFS를 대체 가능한 경우 그렇게 하도록 노력해보자.
'''