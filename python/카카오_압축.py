"""
O(NM)
역시 문자열 처리를 잘 신경쓰면 어렵지 않은 문제였다.
chr을 처음 써봤는데 유용하게 쓸 수 있을 것 같다.
"""


def solution(msg):
    d = {chr(c + 64): c for c in range(1, 27)}
    idx = 27
    answer = []
    i, j = 0, 1
    while True:
        if j > len(msg):
            answer.append(d[msg[i:j - 1]])
            break
        if msg[i:j] in d:
            j += 1
            continue
        else:
            d[msg[i:j]] = idx
            idx += 1
            answer.append(d[msg[i:j - 1]])
            i = j - 1
            j = i + 1
    return answer


print(solution("KAKAO"))