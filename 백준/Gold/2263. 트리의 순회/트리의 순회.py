import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

nodes = [0] * (n + 1)
for i in range(n):
    nodes[inorder[i]] = i

def preorder(in_s, in_e, po_s, po_e):
    if (in_s > in_e) or (po_s > po_e):
        return
    
    root = postorder[po_e]
    
    left = nodes[root] - in_s
    right = in_e - nodes[root]
    
    print(root, end=' ')
    preorder(in_s, in_s + left - 1, po_s, po_s + left - 1)
    preorder(in_e - right + 1, in_e, po_e - right, po_e - 1)

preorder(0, n - 1, 0, n - 1)