"""
O(N)
시뮬레이션 문제.
문제를 잘 읽고 따라하면 되는 문제였다.
문자열 처리를 잘 신경쓰기만 하면 그리 어렵지 않은 문제.
"""
from collections import deque


def solution(dartResult):
    strs, score = deque(), []
    for i in range(len(dartResult) - 1, -1, -1):
        if i == 0:
            strs.appendleft(dartResult)
        elif dartResult[i].isdigit() and not dartResult[i - 1].isdigit():
            strs.appendleft(dartResult[i:])
            dartResult = dartResult[:i]
    for i in range(len(strs)):
        for j in range(len(strs[i])):
            if strs[i][j].isalpha():
                num = int(strs[i][:j])
                if strs[i][j] == "D":
                    num = num ** 2
                elif strs[i][j] == "T":
                    num = num ** 3
                score.append(num)
                if len(strs[i]) > j + 1:
                    if strs[i][j + 1] == "*":
                        score[-1] *= 2
                        if not len(score) == 1:
                            score[-2] *= 2
                    elif strs[i][j + 1] == "#":
                        score[-1] *= -1

    return sum(score)