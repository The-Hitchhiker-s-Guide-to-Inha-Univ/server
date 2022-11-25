from bfs import bfs
import map

map_graph = dict(
    map.East_1,**map.East_2,**map.East_3,**map.East_4,**map.East_5,
    **map.North_1,**map.North_2,**map.North_3,**map.North_4,**map.North_5,
    **map.West_2,**map.West_3,**map.West_4,**map.West_5,
    **map.Stair
)

def get_map_graph():
    return map_graph

def map_text(start, finish):
    # map_graph = dict(
    #     map.East_1,**map.East_2,**map.East_3,**map.East_4,**map.East_5,
    #     **map.North_1,**map.North_2,**map.North_3,**map.North_4,**map.North_5,
    #     **map.West_2,**map.West_3,**map.West_4,**map.West_5,
    #     **map.Stair
    # )

    route = bfs(map_graph,start,finish)

    #print(route)

    result = []

    direction = {"E":"동","W":"서","S":"남","N":"북"}

    for idx, i in enumerate(route):
        if idx == 0:
            result.append(f'5호관 {route[0]}에서 {route[1]}쪽 방향으로 출발')
        elif "계단" in i:
            result.append(f'{i}을 통해 {route[idx-1][2]}층에서 {route[idx+1][2]}층으로 이동하여 {route[idx+1]}까지 이동')
            result.append(f'{route[idx+1]}에서 {route[idx+2]} 방향으로 이동')
        else:
            if idx+1 != len(route) and not "계단" in route[idx+1] and route[idx][1] != route[idx+1][1]:
                result.append(f'{i}까지 이동 후 {direction[route[idx][1]]}쪽 건물에서 {direction[route[idx+1][1]]}쪽 건물로 이동하여 {route[idx+1]}까지 이동')
            elif idx == len(route) - 1:
                result.append(f'{i}까지 이동하여 도착')
            else:
            #result.append(f'5호관 {i}까지 이동')
                if idx + 1 != len(route) and "계단" in route[idx+1]:
                    result.append(f'5호관 {i} 옆 {route[idx+1]}까지 이동')
        

    # for i in result:
    #     print(i)

    return result

#map_text()