n = int(input())
d = []
for i in range(n):
    d.append(list(map(int, input().split())))
dp = [[[-1] * 4 for i in range(n)] for j in range(n)]


def dfs(y, x, p):
    if y == n - 1 and x == n - 1:
        return 1
    else:
        if dp[y][x][p] == -1:
            a, b, c = 0, 0, 0
            if p == 1:
                # 가로
                if 0 <= y < n and 0 <= x + 1 < n and d[y][x + 1] != 1:
                    a = dfs(y, x + 1, 1)
                # 대각선
                if 0 <= y + 1 < n and 0 <= x + 1 < n and d[y + 1][x + 1] != 1 and d[y + 1][x] != 1 and d[y][x + 1] != 1:
                    c = dfs(y + 1, x + 1, 3)
            elif p == 2:
                # 세로
                if 0 <= y + 1 < n and 0 <= x < n and d[y + 1][x] != 1:
                    b = dfs(y + 1, x, 2)
                # 대각선
                if 0 <= y + 1 < n and 0 <= x + 1 < n and d[y + 1][x + 1] != 1 and d[y + 1][x] != 1 and d[y][
                    x + 1] != 1:
                    c = dfs(y + 1, x + 1, 3)
            elif p == 3:
                # 가로
                if 0 <= y < n and 0 <= x + 1 < n and d[y][x + 1] != 1:
                    a = dfs(y, x + 1, 1)
                # 세로
                if 0 <= y + 1 < n and 0 <= x < n and d[y + 1][x] != 1:
                    b = dfs(y + 1, x, 2)
                # 대각선
                if 0 <= y + 1 < n and 0 <= x + 1 < n and d[y + 1][x + 1] != 1 and d[y + 1][x] != 1 and d[y][
                    x + 1] != 1:
                    c = dfs(y + 1, x + 1, 3)
            dp[y][x][p] = a + b + c
        return dp[y][x][p]


print(dfs(0, 1, 1))

'''
1시간
원래는 브루트포스 문제로 그냥 모든 경우를 DFS해보는 문제였지만 이상하게 시간초과가 떠서 DP로 풀어봤음.
훨씬 빠른 시간으로 통과!
'''