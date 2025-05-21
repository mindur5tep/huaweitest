MAX_NODES = 1000
sample_count = [0] * MAX_NODES
n = 0
tree = [[] for _ in range(MAX_NODES)]
visited = [False] * MAX_NODES

def dfs(curr_node, parent_node):
    for child_node in tree[curr_node]:
        if child_node == parent_node:
            continue
        dfs(child_node, curr_node)
        sample_count[curr_node] += sample_count[child_node]

def func():
    global n
    n = int(input())
    curr_node_idx = 1
    child_node_idx = 1

    values = list(map(int, input().strip().split()))

    for value in values:
        if value == -1:
            curr_node_idx += 1
        else:
            sample_count[child_node_idx] = value
            child_node_idx += 1
            if child_node_idx > 2:
                tree[curr_node_idx -1].append(child_node_idx - 1)
                tree[child_node_idx - 1].append(curr_node_idx - 1)
    
    dfs(1,-1)

    result = []
    result.append(sample_count[1])
    result.append(-1)
    visited[1] = True

    for i in range(1, n + 1):
        size = len(tree[i])
        if size > 1:
            for j in range(size):
                child_node = tree[i][j]
                if not visited[child_node]:
                    visited[child_node] = True
                    result.append(sample_count[child_node])
        if i != n:
            result.append(-1)

    print(" ".join(map(str, result)))

if __name__ == "__main__":
    func()
