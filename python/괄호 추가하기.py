n = int(input())
e = list(input())
answer = -9999999999999999999


def dfs(s, pos):
    global answer
    if pos >= len(s):
        i, j = 0, 0
        equation = "".join(s)
        while True:
            if j >= len(equation):
                break
            elif equation[j] == "(":
                i = j
            elif equation[j] == ")":
                equation = equation[:i + 1] + str(eval(equation[i + 1:j])) + equation[j:]
                idx = i + 2
                while True:
                    if equation[idx] == ")":
                        j = idx
                        break
                    else:
                        idx += 1
            j += 1
        idx, cnt = 0, 0
        while True:
            if idx >= len(equation):
                answer = max(answer, eval(equation))
                break
            if equation[idx] in ["*", "-", "+"] and equation[idx - 1] != "(":
                cnt += 1
                if cnt == 2:
                    temp = eval(equation[:idx])
                    if temp < 0:
                        temp = "(" + str(temp) + ")"
                    else:
                        temp = str(temp)
                    equation = str(temp) + equation[idx:]
                    idx, cnt = 0, 0
                else:
                    idx += 1
            else:
                idx += 1
    elif s[pos] not in ["*", "-", "+"]:
        dfs(s, pos + 1)
    else:
        dfs(s, pos + 1)
        idx = -1
        for i in range(pos - 1, -1, -1):
            if i == 0:
                s = ["("] + s
                break
            elif s[i] == ")":
                return
            elif s[i] in ["*", "-", "+"]:
                s = s[:i + 1] + ["("] + s[i + 1:]
                break
            else:
                continue
        for i in range(pos + 2, len(s)):
            if i == len(s) - 1:
                s += [")"]
                idx = i + 2
                break
            elif s[i] in ["*", "-", "+"]:
                s = s[:i] + [")"] + s[i:]
                idx = i + 1
                break
            else:
                continue
        dfs(s, idx)


dfs(e, 0)
print(answer)
