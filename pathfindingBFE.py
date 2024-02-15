from queue import Queue


def my_search(map_data, start):
    frontier = Queue()
    frontier.put(start)
    came_from = {start: None}

    while not frontier.empty():
        current = frontier.get()

        # break the loop if the end goal is found
        if map_data[current[0]][current[1]] == 'D':
            end = current
            break

        for next in get_neighbors(map_data, current):
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current

    # Reconstruct the path from back to the start
    path = []
    current = end
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)  # Add the start position
    path.reverse()  # Reverse the path to start to end

    return path


def get_neighbors(map_data, current):
    # Possible moves: Up, Down, Left, Right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = []
    x, y = current
    rows, cols = len(map_data), len(map_data[0])

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and map_data[nx][ny] != '*':  # Check boundaries and avoid lava
            neighbors.append((nx, ny))
    return neighbors


# if __name__ == '__main__':
#
#     start_row = 14
#     start_col = 16
#     start_position = (start_row, start_col)
#
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
#
#     start_row = 14
#     start_col = 16
#     print(my_search(lava_map1, (start_row, start_col)))
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
#     print(my_search(lava_map2, (start_row2, start_col2)))
#
# if __name__ == '__main__':
#
#     # this tests if the code runs with bigger caves
#     with open("cave300x300") as f:
#         map_data = [l.strip() for l in f.readlines() if len(l) > 1]
#         print(my_search(map_data, (2, 2))) # D location (295, 257)
#
#     with open("cave600x600") as f:
#         map_data = [l.strip() for l in f.readlines() if len(l) > 1]
#         print(my_search(map_data, (2, 2))) # D location 598, 595
#
#
#     with open("cave900x900") as f:
#         map_data = [l.strip() for l in f.readlines() if len(l) > 1]
#         print(my_search(map_data, (2, 2))) # D location 898, 895

if __name__ == '__main__':
    import time

    start_time = time.time()

    with open("cave900x900") as f:
        path = [l.strip() for l in f.readlines() if len(l) > 1]
        print(my_search(path, (2, 2)))

    end_time = time.time()
    time_to_find_solution = end_time - start_time

    print(time_to_find_solution)
    print(len(path))
