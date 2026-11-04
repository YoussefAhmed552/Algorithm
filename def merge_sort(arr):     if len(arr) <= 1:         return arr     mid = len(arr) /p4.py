def find_order(num_courses, prerequisites):
    adj = {i: [] for i in range(num_courses)}
    for dest, src in prerequisites:
        adj[src].append(dest)
    
    visited = [0] * num_courses
    stack = []
    
    def dfs(node):
        if visited[node] == 1:
            return False
        if visited[node] == 2:
            return True
        
        visited[node] = 1
        for neighbor in adj[node]:
            if not dfs(neighbor):
                return False
        visited[node] = 2
        stack.append(node)
        return True

    for i in range(num_courses):
        if visited[i] == 0:
            if not dfs(i):
                return []
    return stack[::-1]

prereqs = [(1, 0), (2, 1), (3, 2)]
print("Course order:", find_order(4, prereqs))
