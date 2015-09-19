class Vertex(object):
    heightOfTree = 0
    def __init__(self, val):
        self.val = val
        self.left = -1
        self.right = -1
        self.height = 0

    def swap(self):
        left = self.left
        self.left = self.right
        self.right = left

    def __str__(self):
        return str(self.val)

def buildTree(Tree):
    root = Vertex(1)
    root.height = 1
    parent = root
    for idx, ele in enumerate(Tree):
        if idx != 0:
            parent = getParent(idx, Tree)
        setChildren(parent, ele[0], ele[1])

    return root

def getParent(idx, Tree):
    elementIdx = 0
    for ele in Tree:
        if ele[0].val != -1:
            elementIdx += 1
            if elementIdx == idx:
                return ele[0]
        if ele[1].val != -1:
            elementIdx += 1
            if elementIdx == idx:
                return ele[1]
    
def setChildren(parent, left, right):
    left.height = parent.height + 1
    parent.left = left
    right.height = parent.height + 1
    parent.right = right
    Vertex.heightOfTree = parent.height + 1


def printInOrderTree(root):
    if root.left != -1:
        printInOrderTree(root.left)

    if root.val != -1:
        print root,

    if root.right != -1:
        root = root.right
        printInOrderTree(root)
    

def swapAt(k, root, Tree):
    if k == 1:
        root.swap()
    else:
        swapAtKDepth(k, Tree)

    i = 2
    h = i * k
    while h < Vertex.heightOfTree:
        swapAtKDepth(h, Tree)
        #printInOrderTree(root)
        #print

        i += 1 
        h = i * k
    

def swapAtKDepth(k, Tree):
    for idx, ele in enumerate(Tree):
        if ele[0].height == k or ele[1].height == k:
            swapKthNode(idx, Tree)

def swapKthNode(k, Tree):
    left = Tree[k][0]
    right = Tree[k][1]
    if isinstance(left, Vertex):
        left.swap();
    if isinstance(right, Vertex):
        right.swap();

N = int(raw_input())
Tree = []
while N > 0:
    Tree.append([Vertex(int(ele)) for ele in raw_input().split() ])
    N -= 1

T = int(raw_input())
SwapAt = []
while T > 0:
    SwapAt.append(input())
    T -= 1

root = buildTree(Tree)
for swapIdx in SwapAt:
    swapAt(swapIdx, root, Tree)
    printInOrderTree(root)
    print
