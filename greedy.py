from queue import PriorityQueue


def greedy(map_data, start, goal):
    frontier = PriorityQueue()
    # Start with priority 0
    frontier.put((0, start))
    came_from = {start: None}

    while not frontier.empty():
        # Get the current node, where the search currently is
        # based on lowest heuristic value
        _, current_node = frontier.get()

        # If goal is found, stop the search
        if current_node == goal:
            break

        # move to the next node
        for next_node in get_neighbors(map_data, current_node):
            if next_node not in came_from:
                priority = h(next_node, goal)
                frontier.put((priority, next_node))
                came_from[next_node] = current_node

    # Make the path
    path = []
    # Check if the goal was reached
    if current_node == goal:
        # Create path from end to start, using B == came_from[A]
        while current_node != start:
            path.append(current_node)
            current_node = came_from[current_node]
        # Include the start position
        path.append(start)
        # Correct the path order
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
#     print(greedy(lava_map1, (start_row, start_col), (1, 13)))
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
#     print(greedy(lava_map2, (start_row2, start_col2), (1, 13)))
#
#     # this tests if the code runs with bigger caves
#     with open("cave300x300") as f:
#         map_data = [l.strip() for l in f.readlines() if len(l) > 1]
#         print(greedy(map_data, (2, 2), (295, 257)))  # D location (295, 257)
#
#     with open("cave600x600") as f:
#         map_data = [l.strip() for l in f.readlines() if len(l) > 1]
#         print(greedy(map_data, (2, 2), (598, 595)))  # D location 598, 595
#
#     with open("cave900x900") as f:
#         map_data = [l.strip() for l in f.readlines() if len(l) > 1]
#         print(greedy(map_data, (2, 2), (898, 895)))  # D location 898, 895

if __name__ == '__main__':
    import time

    start_time = time.time()

    with open("cave300x300") as f:
        path = [l.strip() for l in f.readlines() if len(l) > 1]
        print(greedy(path, (2, 2), (295, 257)))

    end_time = time.time()
    time_to_find_solution = end_time - start_time

    print(time_to_find_solution)
    print(len(path))