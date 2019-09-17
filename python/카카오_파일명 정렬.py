"""
O(NM), N<=1000, M<=100
역시 문자열처리 문제. 집중해서 문자열 인덱스, 정렬 처리를 신경쓰면 별로 어렵지 않은 문제였다.
"""

def solution(files):
    newFiles = []
    for file in files:
        i, j = -1, -1
        for idx, c in enumerate(file):
            if c.isdigit() and i == -1:
                i = idx
            if idx == len(file) - 1:
                j = idx
            elif not c.isdigit() and i != -1:
                j = idx - 1
                break
        newFiles.append([file[:i], file[i:j + 1], file[j + 1:]])
    newFiles.sort(key=lambda x: (x[0].upper(), int(x[1])))
    answer = []
    for file in newFiles:
        answer.append("".join(file))
    return answer