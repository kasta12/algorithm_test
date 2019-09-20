d = []
for i in range(10):
    d.append(list(map(int, input().split())))


def check(y, x):
    size = 0
    for i in range(4, -1, -1):
        if y + i >= 10 or x + i >= 10:
            continue
        else:
            size = i
            break
    for length in range(size + 1, 0, -1):
        found = True
        for i in range(y, y + length):
            for j in range(x, x + length):
                if d[i][j] == 0:
                    found = False
        if found:
            return length - 1


answer = 100
cnt = 0
paper = [5, 5, 5, 5, 5]


def dfs(y, x):
    global answer, cnt
    if y == 9 and x == 10:
        for i in range(10):
            for j in range(10):
                if d[i][j]:
                    return
        answer = min(answer, cnt)
    elif x == 10:
        dfs(y + 1, 0)
    elif not d[y][x]:
        dfs(y, x + 1)
    else:
        limit = check(y, x)
        for i in range(limit, -1, -1):
            if paper[i] == 0:
                continue
            else:
                for ny in range(y, y + i + 1):
                    for nx in range(x, x + i + 1):
                        d[ny][nx] = 0
                paper[i] -= 1
                cnt += 1
                dfs(y, x + 1)
                for ny in range(y, y + i + 1):
                    for nx in range(x, x + i + 1):
                        d[ny][nx] = 1
                paper[i] += 1
                cnt -= 1


dfs(0, 0)
print(answer if answer != 100 else -1)
