# Assessment 3.4: Non-linear Data Structure
# Program for Diagram 1: Binary Tree using my surname LASPUÑA
# (based on my Assessment 3.3)

from collections import deque


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


# ---------- BFS (Breadth-First Search) ----------
# goes level by level, using a queue
def bfs(start):
    path = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        path.append(node.letter)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return path


# ---------- DFS (Depth-First Search - Preorder) ----------
# Root -> Left -> Right, using recursion
def dfs_preorder(node, path):
    if node is None:
        return
    path.append(node.letter)
    dfs_preorder(node.left, path)
    dfs_preorder(node.right, path)


if __name__ == "__main__":
    print("Binary Tree using LASPUÑA")
    print("BFS:", " -> ".join(bfs(root)))

    dfs_path = []
    dfs_preorder(root, dfs_path)
    print("DFS (Preorder):", " -> ".join(dfs_path))