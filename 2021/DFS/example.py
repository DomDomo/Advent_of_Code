G = {"A": ["C"],
     "B": ["C", "E"],
     "C": ["A", "B", "D", "E"],
     "D": ["C"],
     "E": ["C", "B"],
     "F": []}

visited = {node: False for node in G.keys()}

def dfs(at):
    print(at)
    if visited[at]: return
    visited[at] = True

    neighbours = G[at]
    for node in neighbours:
        dfs(node)


def find_all_paths(current, end, path):
    visited[current] = True
    path.append(current)

    if current == end: 
        print(path)
    else:
        neighbours = G[current]
        for node in neighbours:
            if not visited[node]:
                find_all_paths(node, end, path)

    path.pop()
    visited[current] = False

saved_path = []
start_node = "C"
end_node = "E"
#dfs(start_node)
find_all_paths(start_node, end_node, saved_path)