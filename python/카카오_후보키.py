from copy import deepcopy
columns = []
c = [] 
def solution(relation):
    def dfs(idx):
        global columns
        if idx >= len(relation[0]):
            if not columns:
                return
            for i,x in enumerate(relation):
                for j,y in enumerate(relation):
                    if i < j :
                        temp1, temp2 = "",""
                        for k in columns:
                            temp1 += x[k]
                            temp2 += y[k]
                        if temp1 == temp2:
                            return
            c.append(deepcopy(columns))
        else:
            columns.append(idx)
            dfs(idx+1)
            columns.pop()
            dfs(idx+1)
    dfs(0)
    e =  set()
    for i,x in enumerate(c):
        for j,y in enumerate(c):
            if len(x) < len(y):
                temp = set(x) | set(y)
                if len(y) == len(temp):
                    e.add(j)
    return len(c) - len(e)