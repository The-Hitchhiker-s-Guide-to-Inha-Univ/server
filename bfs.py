from collections import deque

def bfs(graph, start, finish):
    queue = deque()

    queue.append(start)

    visited = [start]

    predecessor = {}

    while queue:
        node = queue.popleft()
        visited.append(node)
        if node in graph:
            for i in graph[node]:
                if node_is_visited(visited, i):
                    continue

                if node_is_stair(i):
                    if current_floor_equals_arrival_floor(node,finish):
                        if node_is_not_5S_connect_stair(i):
                            continue

                if node_is_stair(node):
                    if not current_floor_equals_arrival_floor(i,finish):# and not node_is_5s_connection_stair(node):
                        continue

                
                if current_node_is_arrival_node(i,finish):
                    predecessor[i] = node
                    route = make_route_list_from_predecessor(start, finish, predecessor)
                    return route
                
                if node_is_not_in_predecessor(predecessor, i):
                    predecessor[i] = node

                queue.append(i) 

def node_is_visited(visited, i):
    return i in visited

def node_is_not_in_predecessor(predecessor, i):
    return not i in predecessor

def make_route_list_from_predecessor(start, finish, predecessor):
    route = deque()

    route.append(finish)

    cur = predecessor[finish]
    while current_node_is_not_start_node(start, cur):
        route.appendleft(cur)
        cur = predecessor[cur]

    route.appendleft(start)
    return route

def current_node_is_not_start_node(start, cur):
    return cur != start

def current_node_is_arrival_node(i,finish):
    return i == finish

def node_is_not_5S_connect_stair(i):
    _5S_connect_stair = "5남의 동쪽과 서쪽을 이어주는 계단"
    return i != _5S_connect_stair

def current_floor_equals_arrival_floor(node, finish):
    floor_index = 2
    return node[floor_index] == finish[floor_index]

def node_is_stair(i):
    return "계단" in i 

def node_is_5s_connection_stair(node):
    return "5남의 동쪽과 서쪽을 이어주는 계단" == node