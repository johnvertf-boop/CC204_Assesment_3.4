class Node:
    def __init__(self, letter):
        self.letter = letter
        self.left = None
        self.right = None


# ---------- build the tree from my diagram ----------
#           L
#         /   \
#        A     S
#       / \   / \
#      P   U Ñ   A
root = Node("L")
root.left = Node("A")
root.right = Node("S")
root.left.left = Node("P")
root.left.right = Node("U")
root.right.left = Node("Ñ")
root.right.right = Node("A")


# ---------- DFS 1: Preorder (Root -> Left -> Right) ----------
def dfs_preorder(node, path):
    if node is None:
        return
    path.append(node.letter)         # visit root first
    dfs_preorder(node.left, path)    # then the left subtree
    dfs_preorder(node.right, path)   # then the right subtree


# ---------- DFS 2: Inorder (Left -> Root -> Right) ----------
def dfs_inorder(node, path):
    if node is None:
        return
    dfs_inorder(node.left, path)     # left subtree first
    path.append(node.letter)         # then visit root
    dfs_inorder(node.right, path)    # then the right subtree


# ---------- DFS 3: Postorder (Left -> Right -> Root) ----------
def dfs_postorder(node, path):
    if node is None:
        return
    dfs_postorder(node.left, path)   # left subtree first
    dfs_postorder(node.right, path)  # then the right subtree
    path.append(node.letter)         # visit root last


# ---------- DFS using a stack (iterative Preorder) ----------
# same result as recursive preorder, but uses a stack instead of recursion
def dfs_stack(start):
    path = []
    stack = [start]
    while stack:
        node = stack.pop()
        path.append(node.letter)
        # push right first so the left child is popped first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return path


if __name__ == "__main__":
    print("DFS Methods in Tree using LASPUÑA")

    pre = []
    dfs_preorder(root, pre)
    print("Preorder  (Root-Left-Right):", " -> ".join(pre))

    ino = []
    dfs_inorder(root, ino)
    print("Inorder   (Left-Root-Right):", " -> ".join(ino))

    post = []
    dfs_postorder(root, post)
    print("Postorder (Left-Right-Root):", " -> ".join(post))

    print("DFS using Stack (Preorder) :", " -> ".join(dfs_stack(root)))
