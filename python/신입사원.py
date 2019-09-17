tc = int(input())
for i in range(tc):
    n = int(input())
    l = []
    for j in range(n):
        a, b = map(int, input().split())
        l.append([a, b])
    l.sort(key=lambda x: x[0])
    limit = l[0][1]
    count = 0
    for j in l:
        if j[1] <= limit:
            limit = j[1]
            count += 1
    print(count)

