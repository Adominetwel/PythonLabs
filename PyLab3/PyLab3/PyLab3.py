
import random
import time
WALL = "#"
EMPTY = " "


def print_maze(maze, step_info = ""):
    if step_info:
        print(f"\n{step_info}")
    for row in maze:
        print("".join(row))
    print()
    time.sleep(0.5)


def generate_maze(width, height):
    maze = [[EMPTY for _ in range(width)] for _ in range(height)]
    for x in range(width):
        maze[0][x] = WALL
        maze[height - 1][x] = WALL
    for y in range(height):
        maze[y][0] = WALL
        maze[y][width - 1] = WALL
    step_counter = [0]
    print_maze(maze, "Шаг 0: Начальное состояние")
    divide(maze, 1, 1, width - 2, height - 2, step_counter)

    print_maze(maze, "Генерация успешно завершена!")
    return maze


def divide(maze, x1, y1, x2, y2, step_counter):
    width = x2 - x1 + 1
    height = y2 - y1 + 1
    if width < 3 or height < 3:
        return
    if width > height:
        orientation = "vertical"
    elif height > width:
        orientation = "horizontal"
    else:
        orientation = random.choice(["vertical", "horizontal"])
    step_counter[0] += 1
    if orientation == "vertical":
        valid_xs = [x for x in range(x1, x2) if x % 2 == 0]
        if not valid_xs:
            return
        wall_x = random.choice(valid_xs)
        for y in range(y1, y2 + 1):
            maze[y][wall_x] = WALL

        valid_ys = [y for y in range(y1, y2 + 1) if y % 2 != 0]
        passage_y = random.choice(valid_ys)
        maze[passage_y][wall_x] = EMPTY
        print_maze(maze, f"Шаг {step_counter[0]}:")
        divide(maze, x1, y1, wall_x - 1, y2, step_counter)
        divide(maze, wall_x + 1, y1, x2, y2, step_counter)

    else:
        valid_ys = [y for y in range(y1, y2) if y % 2 == 0]
        if not valid_ys:
            return
        wall_y = random.choice(valid_ys)
        for x in range(x1, x2 + 1):
            maze[wall_y][x] = WALL
        valid_xs = [x for x in range(x1, x2 + 1) if x % 2 != 0]
        passage_x = random.choice(valid_xs)
        maze[wall_y][passage_x] = EMPTY
        print_maze(maze, f"Шаг {step_counter[0]}:")
        divide(maze, x1, y1, x2, wall_y - 1, step_counter)
        divide(maze, x1, wall_y + 1, x2, y2, step_counter)



generate_maze(21, 11)