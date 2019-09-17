n = int(input())
scv = list(map(int, input().split(" ")))
scv += [0] * (3 - len(scv))
a, b, c = scv
h = 0
check = [[[[False] * 20 for k in range(61)] for j in range(61)] for i in range(61)]


def cal(x, y):
    return 0 if x - y < 0 else x - y


damage = [9, 3, 1]


def dfs(a, b, c, h):
    if a == 0 and b == 0 and c == 0:
        check[a][b][c][h] = True
    else:
        # 123
        i, na, nb, nc = 0, 0, 0, 0
        if a > 0:
            na = cal(a, damage[i])
            i += 1
        if b > 0:
            nb = cal(b, damage[i])
            i += 1
        if c > 0:
            nc = cal(c, damage[i])

        if not check[na][nb][nc][h + 1]:
            check[na][nb][nc][h + 1] = True
            dfs(na, nb, nc, h + 1)

        # 132
        i, na, nb, nc = 0, 0, 0, 0
        if a > 0:
            na = cal(a, damage[i])
            i += 1
        if c > 0:
            nc = cal(c, damage[i])
            i += 1
        if b > 0:
            nb = cal(b, damage[i])

        if not check[na][nb][nc][h + 1]:
            check[na][nb][nc][h + 1] = True
            dfs(na, nb, nc, h + 1)

        # 213
        i, na, nb, nc = 0, 0, 0, 0
        if b > 0:
            nb = cal(b, damage[i])
            i += 1
        if a > 0:
            na = cal(a, damage[i])
            i += 1
        if c > 0:
            nc = cal(c, damage[i])

        if not check[na][nb][nc][h + 1]:
            check[na][nb][nc][h + 1] = True
            dfs(na, nb, nc, h + 1)

        # 231
        i, na, nb, nc = 0, 0, 0, 0
        if b > 0:
            nb = cal(b, damage[i])
            i += 1
        if c > 0:
            nc = cal(c, damage[i])
            i += 1
        if a > 0:
            na = cal(a, damage[i])
        if not check[na][nb][nc][h + 1]:
            check[na][nb][nc][h + 1] = True
            dfs(na, nb, nc, h + 1)

        # 312
        i, na, nb, nc = 0, 0, 0, 0
        if c > 0:
            nc = cal(c, damage[i])
            i += 1
        if a > 0:
            na = cal(a, damage[i])
            i += 1
        if b > 0:
            nb = cal(b, damage[i])
        if not check[na][nb][nc][h + 1]:
            check[na][nb][nc][h + 1] = True
            dfs(na, nb, nc, h + 1)

        # 321
        i, na, nb, nc = 0, 0, 0, 0
        if c > 0:
            nc = cal(c, damage[i])
            i += 1
        if b > 0:
            nb = cal(b, damage[i])
            i += 1
        if a > 0:
            na = cal(a, damage[i])
        if not check[na][nb][nc][h + 1]:
            check[na][nb][nc][h + 1] = True
            dfs(na, nb, nc, h + 1)


dfs(a, b, c, 0)
for i in range(20):
    if check[0][0][0][i]:
        print(i)
        break

'''
이전 DP문제들과 비슷하지만 케이스를 나눠야 하는 문제.
케이스 나누기만 신경쓰면 크게 어렵지는 않았다.
'''
