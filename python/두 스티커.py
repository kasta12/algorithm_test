h, w = map(int, input().split())
n = int(input())
l = []
for i in range(n):
    a, b = map(int, input().split())
    if not (a > max(h, w) or b > max(h, w)):
        l.append((a, b))
    else:
        n -= 1
test = []

answer = 0


def check(a, b, c, d, e, f):
    if a + b <= e and max(c, d) <= f:
        return True
    else:
        return False


def dfs(idx, cnt):
    global answer
    if cnt == 2:
        a, b = test[0]
        c, d = test[1]
        if not check(a, c, b, d, h, w) and not check(a, c, b, d, w, h) and \
                not check(a, d, b, c, h, w) and not check(a, d, b, c, w, h) and \
                not check(b, c, a, d, h, w) and not check(b, c, a, d, w, h) and \
                not check(b, d, a, c, h, w) and not check(b, d, a, c, w, h):
            return
        else:
            answer = max(answer, a * b + c * d)
    elif idx == n:
        return
    else:
        dfs(idx + 1, cnt)
        test.append(l[idx])
        dfs(idx + 1, cnt + 1)
        test.pop()


dfs(0, 0)
print(answer)
