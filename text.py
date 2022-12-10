from bfs import bfs
import map

map_graph = dict(
    map.East_1,**map.East_2,**map.East_3,**map.East_4,**map.East_5,
    **map.North_1,**map.North_2,**map.North_3,**map.North_4,**map.North_5,
    **map.West_2,**map.West_3,**map.West_4,**map.West_5,
    **map.South_1,**map.South_2,**map.South_3,**map.South_4,**map.South_5,
    **map.Stair
)

def get_map_graph():
    return map_graph

def convert_text(text):
    direction_index = 1
    text_direction = text[direction_index]

    conversion_target = {
        "동":"E","서":"W","남":"S","북":"N",
        "e":"E","w":"W","s":"S","n":"N"
    }

    if text_direction_is_conversion_target(text_direction, conversion_target):
        direction_converted_text = text[0] + conversion_target[text_direction] + text[2:]
        return direction_converted_text
    
    else:
        return text

def text_direction_is_conversion_target(text_direction, conversion_target):
    return text_direction in conversion_target
    
    
def map_text(start, finish):

    route = bfs(map_graph,start,finish)

    result = []

    direction = {"E":"동","W":"서","S":"남","N":"북"}

    direction_index = 1

    floor_index = 2

    for idx, i in enumerate(route):
        if current_node_is_start_of_route(idx):
            result.append(f'5호관 {route[0]}에서 {route[direction_index]}쪽 방향으로 출발')

        elif current_node_is_stair(i):
            if "엘리베이터" in i:
                result.append(f'{i}를 통해 {route[idx-1][floor_index]}층에서 {route[idx+1][floor_index]}층으로 이동하여 {route[idx+1]}까지 이동')
            else:
                result.append(f'{i}을 통해 {route[idx-1][floor_index]}층에서 {route[idx+1][floor_index]}층으로 이동하여 {route[idx+1]}까지 이동')
            result.append(f'{route[idx+1]}에서 {route[idx+2]} 방향으로 이동')

        else:
            if not current_node_is_end_of_route(route,idx):
                if next_node_is_not_stair(route, idx):
                    if current_direction_and_next_direction_are_different(route, idx):
                        result.append(f'{i}까지 이동 후 {direction[route[idx][direction_index]]}쪽 건물에서 {direction[route[idx+1][direction_index]]}쪽 건물로 이동하여 {route[idx+1]}까지 이동')

            elif current_node_is_end_of_route(route, idx):
                result.append(f'{i}까지 이동하여 도착')

            else:
                if not current_node_is_end_of_route(route,idx) and next_node_is_stair(route, idx):
                    result.append(f'5호관 {i} 옆 {route[idx+1]}까지 이동')

    return result

def next_node_is_stair(route, idx):
    return "계단" in route[idx+1]

def current_direction_and_next_direction_are_different(route, idx):
    direction_index = 1
    return route[idx][direction_index] != route[idx+1][direction_index]

def next_node_is_not_stair(route, idx):
    return not "계단" in route[idx+1]

def current_node_is_end_of_route(route, idx):
    return idx == len(route) - 1

def current_node_is_stair(i):
    return "계단" in i

def current_node_is_start_of_route(idx):
    return idx == 0