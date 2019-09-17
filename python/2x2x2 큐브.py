from copy import deepcopy

dc = deepcopy
c = list(map(int, input().split()))


def rotate(i, n):
    if i == 1:
        for j in range(n):
            temp = dc(c)
            c[0] = temp[23]
            c[2] = temp[21]
            c[4] = temp[0]
            c[6] = temp[2]
            c[8] = temp[4]
            c[10] = temp[6]
            c[21] = temp[10]
            c[23] = temp[8]
    elif i == 2:
        for j in range(n):
            temp = dc(c)
            c[12] = temp[20]
            c[13] = temp[21]
            c[4] = temp[12]
            c[5] = temp[13]
            c[16] = temp[4]
            c[17] = temp[5]
            c[20] = temp[16]
            c[21] = temp[17]
    elif i == 3:
        for j in range(n):
            temp = dc(c)
            c[2] = temp[15]
            c[3] = temp[13]
            c[16] = temp[2]
            c[18] = temp[3]
            c[8] = temp[18]
            c[9] = temp[16]
            c[13] = temp[8]
            c[15] = temp[9]


answer = 1
rotate(1, 1)
for i in range(0, 24, 4):
    if not (c[i] == c[i + 1] and c[i + 1] == c[i + 2] and c[i + 2] == c[i + 3]):
        answer = 0
        break
if not answer:
    answer = 1
    rotate(1, 2)
    for i in range(0, 24, 4):
        if not (c[i] == c[i + 1] and c[i + 1] == c[i + 2] and c[i + 2] == c[i + 3]):
            answer = 0
            break
    if not answer:
        answer = 1
        rotate(1, 1)
        rotate(2, 1)
        for i in range(0, 24, 4):
            if not (c[i] == c[i + 1] and c[i + 1] == c[i + 2] and c[i + 2] == c[i + 3]):
                answer = 0
                break
        if not answer:
            answer = 1
            rotate(2, 2)
            for i in range(0, 24, 4):
                if not (c[i] == c[i + 1] and c[i + 1] == c[i + 2] and c[i + 2] == c[i + 3]):
                    answer = 0
                    break
            if not answer:
                answer = 1
                rotate(2, 1)
                rotate(3, 1)
                for i in range(0, 24, 4):
                    if not (c[i] == c[i + 1] and c[i + 1] == c[i + 2] and c[i + 2] == c[i + 3]):
                        answer = 0
                        break
                if not answer:
                    answer = 1
                    rotate(3, 2)
                    for i in range(0, 24, 4):
                        if not (c[i] == c[i + 1] and c[i + 1] == c[i + 2] and c[i + 2] == c[i + 3]):
                            answer = 0
                            break
print(answer)

'''
큐브를 회전하는 경우는 3차원이므로 3가지의 경우가 있다.
반대쪽 회전은 한쪽 3번 회전과 같다.
'''