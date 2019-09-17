"""
시간복잡도가 중요한 문제는 아님
십진수를 다른 n진수로 변환하는 방법을 안다면 크게 어렵지 않은 문제
역시 문자열 처리하는 과정이 들어감.
"""


def solution(n, t, m, p):
    numbers = "0123456789ABCDEF"
    s, num, turn, answer = "", 0, p - m, ""
    for _ in range(t):
        turn += m
        while True:
            if len(s) < turn:
                temp = num
                number = ""
                while True:
                    temp, left = divmod(temp, n)
                    number = str(numbers[left]) + number
                    if not temp:
                        break
                s += number
                num += 1
            else:
                break
        answer += s[turn - 1]
    return answer