"""
일일이 대조하는 방법을 사용하면 시간복잡도가 O(NL)이므로 불가능하다.
정렬을 통해 사전식 배열로 만든다음 각 단어의 위아래 단어와 대조하고 큰 수를 더하면 정답을 얻을 수 있다는 아이디어를 캐치하는 것이 중요했다.
이 경우 시간복잡도는 O(2L)으로 훨씬 줄어들게 된다.
"""


def solution(words):
    words.sort()
    answer = 0
    for idx, word in enumerate(words):
        val1, val2 = -1, -1
        if 0 <= idx - 1:
            changed = False
            for i in range(min(len(words[idx - 1]), len(word))):
                if words[idx - 1][i] != word[i]:
                    changed = True
                    val1 = i + 1
                    break
            if not changed:
                val1 = len(words[idx - 1]) + 1
        if idx + 1 < len(words):
            changed = False
            for i in range(min(len(words[idx + 1]), len(word))):
                if words[idx + 1][i] != word[i]:
                    changed = True
                    val2 = i + 1
                    break
            if not changed:
                val2 = len(word)
        answer += max(val1, val2)
    return answer