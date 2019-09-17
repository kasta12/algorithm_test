tc = []
d = [[0] * 31 for i in range(31)]
for i in range(30):
    d[0][i] = 1
while True:
    temp = int(input())
    if temp != 0:
        tc.append(temp)
    else:
        break
val = max(tc)


def go(f, h):
    if f == 0:
        return 1
    elif h == 0:
        if d[f][0] == 0:
            d[f][0] = go(f - 1, 1)
        return d[f][0]
    elif d[f][h] != 0:
        return d[f][h]
    else:
        if d[f - 1][h + 1] == 0:
            d[f - 1][h + 1] = go(f - 1, h + 1)
        if d[f][h - 1] == 0:
            d[f][h - 1] = go(f, h - 1)
        return d[f - 1][h + 1] + d[f][h - 1]


for i in tc:
    print(go(i, 0))

'''
DP문제이고 역시 상태를 정확히 정의하는게 중요했다.
현재 상태를 d[한알개수][반알개수]로 정의했고 피보나치 수열처럼 상태끼리의 관계를 나타내는게 중요했다.
'''