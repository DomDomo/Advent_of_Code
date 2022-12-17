lines = []

with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

edges = []
vertecies = set()
for edge in lines:
    a, b = edge.split("-")
    vertecies.add(a)
    vertecies.add(b)
    edges.append((a, b))


G = {
    "start": ["A", "b"],
    "c": ["A"],
    "A": ["c", "start", "b", "end"],
    "b": ["A", "start", "d", "end"],
    "d": ["b"],
    "end": ["A", "b"]
}

G = {node: [] for node in vertecies}
for edge in edges:
    a, b = edge
    G[a].append(b)
    G[b].append(a)


visited = {node: 0 for node in G.keys()}

def find_all_paths(current, end, path):
    visited[current] += 1
    path.append(current)

    if current == end:
        all_paths.append(path.copy())
    else:
        neighbours = G[current]
        for node in neighbours:
            if not node.islower() or visited[node] < 1:
                find_all_paths(node, end, path)

    path.pop()
    visited[current] = False

all_paths = []
saved_path = []
start_node = "start"
end_node = "end"
find_all_paths(start_node, end_node, saved_path)

print(G)

for path in all_paths:
    print(path)
print(len(all_paths))