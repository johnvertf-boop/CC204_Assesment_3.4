# Assessment 3.4: Non-linear Data Structure
# Program for Diagram 2: Graph using my surname LASPUÑA
# (based on my Assessment 3.3)
# A1 and A2 are the two A letters in LASPUÑA

from collections import deque

# ---------- edges (connections) from my diagram ----------
edges = [
    ("L", "A1"),
    ("L", "P"),
    ("A1", "S"),
    ("A1", "A2"),
    ("S", "Ñ"),
    ("Ñ", "U"),
    ("U", "P"),
    ("A2", "Ñ"),
    ("S", "A2"),
]

# ---------- adjacency list (undirected graph) ----------
graph = {}
for a, b in edges:
    graph.setdefault(a, []).append(b)
    graph.setdefault(b, []).append(a)


# ---------- BFS (Breadth-First Search) ----------
# visits the nearest letters first, using a queue
def bfs(start):
    visited = [start]
    queue = deque([start])
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
    return visited


# ---------- DFS (Depth-First Search) ----------
# follows one path as deep as possible, then backtracks (recursion)
def dfs(current, visited):
    visited.append(current)
    for neighbor in graph[current]:
        if neighbor not in visited:
            dfs(neighbor, visited)


if __name__ == "__main__":
    print("Graph using LASPUÑA (starting at L)")
    print("Adjacency list:")
    for letter in graph:
        print(" ", letter, ":", ", ".join(graph[letter]))

    print("BFS:", " -> ".join(bfs("L")))

    dfs_path = []
    dfs("L", dfs_path)
    print("DFS:", " -> ".join(dfs_path))