import argparse
import pygame
import random
import sys
import os

DEFAULT_WIDTH = 60
DEFAULT_HEIGHT = 30
DEFAULT_FPS = 10

WIDTH = DEFAULT_WIDTH
HEIGHT = DEFAULT_HEIGHT
FPS = DEFAULT_FPS
CELL_SIZE = 15
SCREEN_WIDTH = WIDTH * CELL_SIZE
SCREEN_HEIGHT = HEIGHT * CELL_SIZE + 40
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (50, 205, 50)
GRAY = (70, 70, 70)

def initialize_game(width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT, fps=DEFAULT_FPS):
    global WIDTH, HEIGHT, FPS, SCREEN_WIDTH, SCREEN_HEIGHT, screen, clock, font
    WIDTH = width
    HEIGHT = height
    FPS = fps
    SCREEN_WIDTH = WIDTH * CELL_SIZE
    SCREEN_HEIGHT = HEIGHT * CELL_SIZE + 40
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Conway's Game of Life - Project 1")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('Arial', 16)
    return [[0] * WIDTH for _ in range(HEIGHT)]

def count_neighbors(board, x, y):
    height = len(board)
    width = len(board[0])
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            nx, ny = (x + i) % width, (y + j) % height
            if board[ny][nx] == 1:
                count += 1
    return count

def next_gen(board):
    height = len(board)
    width = len(board[0])
    new_board = [[0] * width for _ in range(height)]
    for y in range(height):
        for x in range(width):
            neighbors = count_neighbors(board, x, y)
            if board[y][x] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_board[y][x] = 0
                else:
                    new_board[y][x] = 1
            else:
                if neighbors == 3:
                    new_board[y][x] = 1
    return new_board

def draw_board(board, generation, running):
    screen.fill(BLACK)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if board[y][x] == 1:
                pygame.draw.rect(screen, GREEN, rect)
            pygame.draw.rect(screen, GRAY, rect, 1)
    pygame.draw.rect(screen, WHITE, (0, HEIGHT * CELL_SIZE, SCREEN_WIDTH, 40))
    pygame.draw.rect(screen, BLACK, (0, HEIGHT * CELL_SIZE, SCREEN_WIDTH, 40), 2)
    status = "▶ Running" if running else "⏸ Paused"
    live_cells = 0
    for row in board:
        for cell in row:
            if cell == 1:
                live_cells += 1
    controls_text = "Space:▶/⏸  N:Step  R:Random  C:Clear  S:Save  L:Load"
    status_text = f"Gen: {generation}  Live: {live_cells}  FPS: {FPS}"
    controls_surface = font.render(controls_text, True, BLACK)
    status_surface = font.render(status_text, True, BLACK)
    screen.blit(controls_surface, (10, HEIGHT * CELL_SIZE + 5))
    screen.blit(status_surface, (10, HEIGHT * CELL_SIZE + 25))
    pygame.display.flip()

def randomize_board(board):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            board[y][x] = 1 if random.random() < 0.3 else 0
    return board

def clear_board():
    return [[0] * WIDTH for _ in range(HEIGHT)]

def save_pattern(board):
    try:
        live_cells = []
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if board[y][x] == 1:
                    live_cells.append(f"{x},{y}")
        with open("patterns.txt", "w") as f:
            f.write("# Pattern: Saved Game\n")
            f.write("\n".join(live_cells))
        print("Pattern saved to patterns.txt")
    except Exception as e:
        print(f"Error saving pattern: {e}")

def load_pattern():
    if not os.path.exists("patterns.txt"):
        print("patterns.txt not found")
        return clear_board()
    board = clear_board()
    with open("patterns.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                try:
                    x, y = map(int, line.split(","))
                    if 0 <= x < WIDTH and 0 <= y < HEIGHT:
                        board[y][x] = 1
                except ValueError:
                    print(f"Invalid line: {line}")
    return board

def main():
    parser = argparse.ArgumentParser(description="Conway's Game of Life")
    parser.add_argument('--width', type=int, default=DEFAULT_WIDTH, help='Width of the board')
    parser.add_argument('--height', type=int, default=DEFAULT_HEIGHT, help='Height of the board')
    parser.add_argument('--fps', type=int, default=DEFAULT_FPS, help='Frames per second')
    args = parser.parse_args()
    board = initialize_game(args.width, args.height, args.fps)
    generation = 0
    running = False
    board[1][0] = 1
    board[2][1] = 1
    board[0][2] = 1 
    board[1][2] = 1
    board[2][2] = 1
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                elif event.key == pygame.K_n:
                    board = next_gen(board)
                    generation += 1
                elif event.key == pygame.K_r:
                    board = randomize_board(board)
                    generation = 0
                elif event.key == pygame.K_c:
                    board = clear_board()
                    generation = 0
                elif event.key == pygame.K_s:
                    save_pattern(board)
                elif event.key == pygame.K_l:
                    board = load_pattern()
                    generation = 0
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos[0] // CELL_SIZE, event.pos[1] // CELL_SIZE
                if 0 <= x < WIDTH and 0 <= y < HEIGHT:
                    board[y][x] = 1 - board[y][x]
        if running:
            board = next_gen(board)
            generation += 1
        draw_board(board, generation, running)
        clock.tick(FPS)

if __name__ == "__main__":
    main()