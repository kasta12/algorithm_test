a, b, c, x, y = map(int, input().split())
if a + b < c * 2:
    print(a * x + b * y)
else:
    total = 0
    m, l = min(x, y), max(x, y)
    total += m * c * 2
    left = l - m
    if x > y:
        val = a
    else:
        val = b
    if val > c * 2:
        total += left * c * 2
    else:
        total += left * val
    print(total)
