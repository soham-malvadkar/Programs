from collections import deque

graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input("Enter node name: ")

    neighbors = input(
        f"Enter neighbors of {node} separated by space: "
    ).split()

    graph[node] = neighbors

def dfs(graph, node, visited=None):

    if visited is None:
        visited = set()

    if node not in graph:
        print(f"\nNode '{node}' not found in graph")
        return

    visited.add(node)

    print(node, end=" ")

    for neighbor in graph[node]:

        if neighbor not in visited:

            dfs(graph, neighbor, visited)

def bfs(graph, start):

    if start not in graph:
        print(f"\nNode '{start}' not found in graph")
        return

    visited = set([start])

    queue = deque([start])

    while queue:

        node = queue.popleft()

        print(node, end=" ")

        for neighbor in graph[node]:

            if neighbor not in visited:

                visited.add(neighbor)

                queue.append(neighbor)

start = input("Enter starting node: ")

print("\nDFS Traversal:")
dfs(graph, start)

print("\nBFS Traversal:")
bfs(graph, start)
