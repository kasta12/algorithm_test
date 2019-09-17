n = int(input())
a, b = [], []  # 내구도, 무게
for i in range(n):
    aa, bb = map(int, input().split())
    a.append(aa)
    b.append(bb)
answer = 0


def dfs(idx):
    global answer
    if idx == n:
        cnt = 0
        for i in a:
            if i <= 0:
                cnt += 1
        answer = max(answer, cnt)
    else:
        if not a[idx] <= 0:
            hit = False
            for i in range(n):
                if i != idx and a[i] > 0:
                    hit = True
                    a[i] -= b[idx]
                    a[idx] -= b[i]
                    dfs(idx + 1)
                    a[i] += b[idx]
                    a[idx] += b[i]
            if not hit:
                dfs(idx + 1)
        else:
            dfs(idx + 1)


dfs(0)
print(answer)
