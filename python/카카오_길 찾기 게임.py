import sys
sys.setrecursionlimit(1000000)

def preorder(subtree, result):  # root -> left -> right
    if len(subtree) != 0:
        left, right = [], []
        for x in subtree[1:]: left.append(x) if x[0] < subtree[0][0] else right.append(x)
        result.append(subtree[0][2]) # root
        preorder(left,result)        # left
        preorder(right,result)       # right
        
def postorder(subtree, result): # left -> right -> root
    if len(subtree) != 0:
        left, right = [], []
        for x in subtree[1:]: left.append(x) if x[0] < subtree[0][0] else right.append(x)
        postorder(left,result)       # left
        postorder(right,result)      # right
        result.append(subtree[0][2]) # root
        
def solution(nodeinfo):
    for i,x in enumerate(nodeinfo): x += [i+1] # 노드에 인덱스 추가하기
    nodeinfo = sorted(nodeinfo,key=lambda x:(-x[1],x[0])) # nodeinfo 0:x좌표 1:y좌표 2:인덱스
    result1, result2 = [], []
    preorder(nodeinfo,result1)
    postorder(nodeinfo,result2)
    return [result1,result2]