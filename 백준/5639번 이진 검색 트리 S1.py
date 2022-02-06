from sys import stdin
import sys
sys.setrecursionlimit(10000)
#트리 만들기
def make_tree(nodes):
    tree = {}
    for i in nodes:
        tree[i] = [None, None]

    root = nodes[0]
    #make tree
    for i in range(1, len(nodes)):
        now = root
        while True:
            if nodes[i] < now:
                if tree[now][0] == None:
                    tree[now][0] = nodes[i]
                    break
                else:
                    now = tree[now][0]
            else:
                if tree[now][1] == None:
                    tree[now][1] = nodes[i]
                    break
                else:
                    now = tree[now][1]
    return tree

#후위 순회
result = ''
def lrp(tree, now):
    global result
    if tree[now][0]:
        lrp(tree, tree[now][0])
    if tree[now][1]:
        lrp(tree, tree[now][1])
    result = result + str(now) + '\n'

#nodes info
nodes = []
while True:
    try:
        nodes.append(int(stdin.readline()))
    except:
        break

tree = make_tree(nodes)
lrp(tree, nodes[0])
print(result)


'''
50
30
24
5
28
45
98
52
60



'''