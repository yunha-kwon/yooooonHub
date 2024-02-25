import sys

N = int(sys.stdin.readline())
left = [0]*(N+1)
right = [0]*(N+1)
tree = {}

for _ in range(N):
    v, l, r = sys.stdin.readline().split()
    tree[v] = [l, r]

def preorder(v):
    if v != '.':
        print(v, end='')
        preorder(tree[v][0])
        preorder(tree[v][1])

def inorder(v):
    if v != '.':
        inorder(tree[v][0])
        print(v, end='')
        inorder(tree[v][1])

def postorder(v):
    if v != '.':
        postorder(tree[v][0])
        postorder(tree[v][1])
        print(v, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')