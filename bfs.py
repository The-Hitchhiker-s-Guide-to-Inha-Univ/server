from collections import deque
import copy

def bfs(graph, start, finish):
    queue = deque()

    queue.append((start,[start]))

    visited = [start]

    while queue:
        node,route = queue.popleft()
        visited.append(node)
        if node in graph:
            for i in graph[node]:
                if i in visited:
                    continue
                temp_route = copy.deepcopy(route)
                if i == finish:
                    temp_route.append(i)
                    return temp_route
                # if i in ("남동쪽 계단","동쪽 중앙 계단","북동쪽 계단"):
                #     temp_route.append(i)
                temp_route.append(i)
                queue.append((i,temp_route))    