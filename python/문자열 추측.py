n = int(input())
l = []
a, b, c = [], [], []
for i in range(2 * n - 2):
    temp = input()
    if len(temp) == 1:
        a.append(temp)
    elif len(temp) == n - 1:
        b.append(temp)
    l.append(temp)
if not b:
    c.extend([a[0] + a[1], a[1] + a[0]])
else:
    for i in a:
        for j in b:
            c.append(i + j)
for s in c:
    ps = []
    isP = [False] * n
    found = True
    for st in l:
        prefix, suffix = s[:len(st)], s[len(s) - len(st):]
        if st == prefix and st == suffix:
            if not isP[len(st)]:
                ps.append("P")
                isP[len(st)] = True
            else:
                ps.append("S")
        elif st == prefix:
            ps.append("P")
        elif st == suffix:
            ps.append("S")
        else:
            found = False
            ps.clear()
            break
    if found:
        print(s)
        print("".join(ps))
        break
