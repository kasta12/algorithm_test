"""
O(N^2)
문자열의 최대길이가 1000이므로 N^2의 시간안에 해결 가능
두 자리씩 끊어서 리스트를 만든 후 모든 문자열 비교
"""


def solution(str1, str2):
    l1, l2 = [], []
    for i in range(len(str1) - 1):
        temp = str1[i:i + 2]
        if temp.isalpha():  # 두 자리가 모두 알파벳인 경우만 취급
            l1.append(temp.upper())
    for i in range(len(str2) - 1):
        temp = str2[i:i + 2]
        if temp.isalpha():  # 두 자리가 모두 알파벳인 경우만 취급
            l2.append(temp.upper())
    if not l1 and not l2:  # 두 집합이 공집합인 경우 자카드 유사도가 1
        return 65536
    u, n = 0, 0
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i] == l2[j]:
                l2[j] = "--"  # 겹치는 것이 있으면 다음 계산에 포함되지 않도록 처리
                n += 1  # 겹치는 횟수 증가
                break
    u = len(l1) + len(l2) - n
    return n * 65536 // u