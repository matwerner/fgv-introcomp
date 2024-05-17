import os

def generate_maze():
    maze = [
        "XXXXXXXXXXXXXXXX",
        "X       X      X",
        "X XXXXX X XXXX X",
        "X XXXXX X XXXX X",
        "X XXXXX X XXXX X",
        "X              X",
        "X XXXXX X XXXX X",
        "X XXXXX X XXXX X",
        "X XXXXX X XXXX X",
        "X       X      X",
        "XXXXXXXXXXXXXXXX"
    ]
    maze = [[cell for cell in row]
            for row in maze]
    return maze

# Função para desenhar o labirinto
def draw_maze(maze: list[list[str]]):
    os.system("cls")
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            print(cell, end="")
        print()
            

def get_input() -> str:
    key = input()
    if key == "w":
        return "UP"
    elif key == "s":
        return "DOWN"
    elif key == "a":
        return "LEFT"
    elif key == "d":
        return "RIGHT"
    return None

def move_player(maze: list[list[str]], player_pos: tuple, direction: str) -> list:
    x, y = player_pos
    if direction == "UP":
        if maze[y - 1][x] != "X":
            maze[y][x] = " "
            maze[y - 1][x] = "P"
            player_pos = (x, y - 1)
    elif direction == "DOWN":
        if maze[y + 1][x] != "X":
            maze[y][x] = " "
            maze[y + 1][x] = "P"
            player_pos = (x, y + 1)
    elif direction == "LEFT":
        if maze[y][x - 1] != "X":
            maze[y][x] = " "
            maze[y][x - 1] = "P"
            player_pos = (x - 1, y)
    elif direction == "RIGHT":
        if maze[y][x + 1] != "X":
            maze[y][x] = " "
            maze[y][x + 1] = "P"
            player_pos = (x + 1, y)
    return maze, player_pos

def path_finder(maze: list[list[str]], player_pos: tuple, target_pos: tuple) -> list[tuple]:
    def is_valid_move(x, y):
        return 0 <= x < len(maze[0]) and 0 <= y < len(maze) and maze[y][x] != "X"
    
    already_visited = set()
    queue = [(player_pos, [])]
    while queue:
        (x, y), path = queue.pop(0)
        if (x, y) == target_pos:
            return path
        if (x, y) in already_visited or not is_valid_move(x, y):
            continue
        already_visited.add((x, y))
        queue.append(((x + 1, y), path + ["RIGHT"]))
        queue.append(((x - 1, y), path + ["LEFT"]))
        queue.append(((x, y + 1), path + ["DOWN"]))
        queue.append(((x, y - 1), path + ["UP"]))
    return []


# Função principal do jogo
def main():
    maze = generate_maze()  # Gerando o labirinto
    player_pos = [1, 1]  # Posição inicial do jogador
    x, y = player_pos
    maze[y][x] = "P"  # Inserindo o jogador no labirinto

    path = path_finder(maze, player_pos, (10, 10))
    print(path)

    while True:
        draw_maze(maze)
        direction = get_input()
        maze, player_pos = move_player(maze, player_pos, direction)

# Chamando a função principal
if __name__ == "__main__":
    main()