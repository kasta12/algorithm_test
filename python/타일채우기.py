import sys

sys.setrecursionlimit(100000)
n = int(input())


def go(num):
    if num == 0:
        return 1
    elif num == 2:
        return 3
    else:
        temp = go(2) * go(num - 2)
        num -= 4
        while num >= 0:
            temp += 2 * go(num)
            num -= 2
        return temp


if n % 2 == 1:
    print(0)
else:
    print(go(n))
