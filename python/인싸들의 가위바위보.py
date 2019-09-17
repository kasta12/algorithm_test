n, k = map(int, input().split(' '))
m = []
for i in range(n):
    m.append(list(map(int, input().split(' '))))

a = [False for i in range(n)]
b = list(map(int, input().split(' ')))
c = list(map(int, input().split(' ')))


def dfs(first, second, nb, nc, va, vb, vc):
    if va == k:
        print(1)
        exit()
    elif vb == k or vc == k:
        return
    else:
        if first == 'a' and second == 'b':
            for i in range(n):
                if a[i]:
                    continue
                a[i] = True
                if m[i][b[nb] - 1] == 2:  # a가 이긴 경우
                    dfs('a', 'c', nb + 1, nc, va + 1, vb, vc)
                else:
                    dfs('b', 'c', nb + 1, nc, va, vb + 1, vc)
                a[i] = False
        elif first == 'b' and second == 'c':
            if m[b[nb] - 1][c[nc] - 1] == 2:  # b가 이긴 경우
                dfs('a', 'b', nb + 1, nc + 1, va, vb + 1, vc)
            else:
                dfs('a', 'c', nb + 1, nc + 1, va, vb, vc + 1)
        elif first == 'a' and second == 'c':
            for i in range(n):
                if a[i]:
                    continue
                a[i] = True
                if m[i][c[nc] - 1] == 2:  # a가 이긴 경우
                    dfs('a', 'b', nb, nc + 1, va + 1, vb, vc)
                else:
                    dfs('b', 'c', nb, nc + 1, va, vb, vc + 1)
                a[i] = False


dfs('a', 'b', 0, 0, 0, 0, 0)
print(0)

'''
신기한 문제여서 풀어봤는데 생각보다 간단했다.
물론 문제를 잘못봐서 좀 오래걸리긴 했다. 항상 느끼지만 문제를 제대로 읽고 풀어야 겠다.
좀 더 복잡해 질 수 있는 문제인데 난이도 조절을 한 듯 하다.
a 를 중심으로 dfs를 구성하여 문제를 해결했다. 경로체크 부분에서 boolean 리스트를 선언하여 방문 여부를 체크했다.
경로 발견한 경우 프로그램을 바로 종료시키기 위해 결과를 출력하고 exit()함수를 사용했다.
'''