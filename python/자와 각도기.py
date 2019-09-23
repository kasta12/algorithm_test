from collections import deque

n, k = map(int, input().split())
a, b = list(map(int, input().split())), list(map(int, input().split()))
check = [False] * 361
q = deque()
for num in a:
    q.append(num)
    check[num], check[360 - num] = True, True
while q:
    angle = q.popleft()
    for alpha in a:
        na = angle + alpha
        if na > 360:
            na -= 360
        if not check[na]:
            check[na], check[360 - na] = True, True
            q.append(min(na, 360 - na))
            a.append(min(na, 360 - na))
        na = abs(angle - alpha)
        if not check[na]:
            check[na], check[360 - na] = True, True
            q.append(min(na, 360 - na))
            a.append(min(na, 360 - na))
for answer in b:
    if check[answer]:
        print("YES")
    else:
        print("NO")
