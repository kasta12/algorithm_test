check = [False] * 1001
n = int(input())
cur = []


def dfs(cnt, s):
    if cnt == 4:
        cur.append(n - s)
        result = cur[0] + cur[1] * 5 + cur[2] * 10 + cur[3] * 50
        if not check[result]:
            check[result] = True
        cur.pop()
    else:
        for i in range(n + 1):
            if s + i > n:
                break
            else:
                cur.append(i)
                dfs(cnt + 1, s + i)
                cur.pop()


dfs(1, 0)
answer = [True for i in check if i]
print(len(answer))
