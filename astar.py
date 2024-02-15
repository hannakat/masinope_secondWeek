from queue import PriorityQueue


def astar(map_data, start, goal):
    # nodes to explore (not visited yet)
    frontier = PriorityQueue()
    # Start with priority 0 for the start node
    frontier.put((0, start))
    # visited nodes and their "neighbours"
    came_from = {start: None}
    cost_so_far = {start: 0}

    while not frontier.empty():

        _, current = frontier.get()

        # Check if the goal has been reached
        if current == goal:
            break

        for next in get_neighbors(map_data, current):
            # cost for moving to a neighbor is always 1
            new_cost = cost_so_far[current] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                #
                priority = new_cost + h(next, goal)
                frontier.put((priority, next))
                came_from[next] = current

    # Reconstruct the path from goal to start
    path = []
    if current == goal:
        while current != start:
            path.append(current)
            current = came_from[current]
        # Add the start position
        path.append(start)
        # Path from start to goal
        path.reverse()
    else:
        path = ["Goal not reachable"]
    return path


def get_neighbors(map_data, current):
    # Possible moves: Up, Down, Left, Right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = []
    x, y = current
    rows, cols = len(map_data), len(map_data[0])

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        # Check boundaries and avoid lava
        if 0 <= nx < rows and 0 <= ny < cols and map_data[nx][ny] != '*':
            neighbors.append((nx, ny))
    return neighbors


def h(node, goal):
    # Manhattan distance between node and goal
    # (node x value - goal x value) + (node y value - goal y value)
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])


# if __name__ == '__main__':
#     lava_map1 = [
#         "      **               **      ",
#         "     ***     D        ***      ",
#         "     ***                       ",
#         "                      *****    ",
#         "           ****      ********  ",
#         "           ***          *******",
#         " **                      ******",
#         "*****             ****     *** ",
#         "*****              **          ",
#         "***                            ",
#         "              **         ******",
#         "**            ***       *******",
#         "***                      ***** ",
#         "                               ",
#         "                s              ",
#     ]
#     start_row = 14
#     start_col = 16
#     print(astar(lava_map1, (start_row, start_col), (1, 13)))
#
#     lava_map2 = [
#         "     **********************    ",
#         "   *******   D    **********   ",
#         "   *******                     ",
#         " ****************    **********",
#         "***********          ********  ",
#         "            *******************",
#         " ********    ******************",
#         "********                   ****",
#         "*****       ************       ",
#         "***               *********    ",
#         "*      ******      ************",
#         "*****************       *******",
#         "***      ****            ***** ",
#         "                               ",
#         "                s              ",
#     ]
#     start_row2 = 14
#     start_col2 = 16
#     print(astar(lava_map2, (start_row2, start_col2), (1, 13)))
#
#     # this tests if the code runs with bigger caves
#     with open("cave300x300") as f:
#         map_data = [l.strip() for l in f.readlines() if len(l) > 1]
#         print(astar(map_data, (2, 2), (295, 257)))  # D location (295, 257)
#
#     with open("cave600x600") as f:
#         map_data = [l.strip() for l in f.readlines() if len(l) > 1]
#         print(astar(map_data, (2, 2), (598, 595)))  # D location 598, 595
#
#     with open("cave900x900") as f:
#         map_data = [l.strip() for l in f.readlines() if len(l) > 1]
#         print(astar(map_data, (2, 2), (898, 895)))  # D location 898, 895

if __name__ == '__main__':
    import time

    start_time = time.time()

    with open("cave900x900") as f:
        path = [l.strip() for l in f.readlines() if len(l) > 1]
        print(astar(path, (2, 2), (898, 895)))  # D location 898, 895

    end_time = time.time()
    time_to_find_solution = end_time - start_time

    print(time_to_find_solution)
    print(len(path))
