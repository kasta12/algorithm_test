"""
O(N^2)이지만 N이 최대 16이므로 걱정 안해도 된다.
2진수 처리하는 방법을 조금만 생각해보면 쉬운 문제
divmod를 사용하여 쉽게 해결
"""


def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        d1, d2 = arr1[i], arr2[i]
        line = ""
        for j in range(n - 1, -1, -1):
            a1, b1 = divmod(d1, 2 ** j)
            a2, b2 = divmod(d2, 2 ** j)
            if a1 or a2:
                line += "#"
            else:
                line += " "
            d1, d2 = b1, b2
        answer.append(line)
    return answer