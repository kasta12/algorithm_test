from itertools import combinations

n, m = map(int, input().split())
check = [[False] * 200 for _ in range(200)]
for i in range(m):
    a, b = map(int, input().split())
    check[a - 1][b - 1] = True
    check[b - 1][a - 1] = True
ic = combinations(range(n), 3)
answer = 0
for com in ic:
    group = combinations(com, 2)
    found = True
    for a, b in group:
        if check[a][b]:
            found = False
            break
    if found:
        answer += 1
print(answer)
