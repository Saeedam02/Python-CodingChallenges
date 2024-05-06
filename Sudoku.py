import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((450, 450))
pygame.display.set_caption("Sudoku Game")

# Constants
BASE = 3
SIDE = BASE * BASE
CELL_SIZE = 50
GRID_SIZE = CELL_SIZE * SIDE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_GRAY = (220, 220, 220)
HIGHLIGHT = (160, 160, 255)
GREEN = (0, 255, 0)

# Font
font = pygame.font.Font(None, 40)

def generate_board():
    base = 3
    side = base * base
    def pattern(r, c): return (base * (r % base) + r // base + c) % side
    def shuffle(s): return random.sample(s, len(s))
    rBase = range(base)
    rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
    cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
    nums = shuffle(range(1, base * base + 1))

    board = [[nums[pattern(r, c)] for c in cols] for r in rows]
    user_inputs = [[False] * side for _ in range(side)]  # Track user inputs

    squares = side * side
    empties = int(squares * 0.5)
    for p in random.sample(range(squares), empties):
        board[p // side][p % side] = 0

    return board, user_inputs

def draw_grid(board, user_inputs, selected=None):
    for i in range(SIDE):
        for j in range(SIDE):
            x = j * CELL_SIZE
            y = i * CELL_SIZE
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, WHITE if (i + j) % 2 == 0 else LIGHT_GRAY, rect)
            if board[i][j] != 0:
                color = GREEN if user_inputs[i][j] else BLACK
                text = font.render(str(board[i][j]), True, color)
                text_rect = text.get_rect(center=rect.center)
                screen.blit(text, text_rect)

    for i in range(0, GRID_SIZE, CELL_SIZE):
        line_width = 1 if i % (CELL_SIZE * BASE) else 2
        pygame.draw.line(screen, BLACK, (i, 0), (i, GRID_SIZE), line_width)
        pygame.draw.line(screen, BLACK, (0, i), (GRID_SIZE, i), line_width)

    if selected:
        pygame.draw.rect(screen, HIGHLIGHT, (selected[1]*CELL_SIZE, selected[0]*CELL_SIZE, CELL_SIZE, CELL_SIZE), 3)

def check_win(board):
    """Check if all cells are filled correctly according to Sudoku rules."""
    for i in range(SIDE):
        for j in range(SIDE):
            num = board[i][j]
            if num == 0 or not valid(board, num, (i, j)):
                return False
    return True
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

def valid(board, num, pos):
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0

    return False

def display_win_message():
    YELLOW = (255, 255, 0)  # RGB for yellow
    larger_font = pygame.font.Font(None, 72)
    win_text = larger_font.render("You Win!", True, YELLOW)
    win_text_rect = win_text.get_rect(center=(GRID_SIZE // 2, GRID_SIZE // 2))
    # Draw a black rectangle behind the text for better visibility
    background_rect = win_text_rect.inflate(20, 10)  # Slightly larger rect for background
    pygame.draw.rect(screen, BLACK, background_rect)  # Draw the black background rectangle
    screen.blit(win_text, win_text_rect)



def main():
    global board, user_inputs
    board, user_inputs = generate_board()
    selected_cell = None
    running = True
    game_won = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                selected_cell = (pos[1] // CELL_SIZE, pos[0] // CELL_SIZE)
            elif event.type == pygame.KEYDOWN:
                if selected_cell:
                    if event.key == pygame.K_s:  # Solve the board
                        solve(board)
                        user_inputs = [[True] * SIDE for _ in range(SIDE)]
                        game_won = check_win(board)
                    elif event.unicode.isdigit() and '1' <= event.unicode <= '9':
                        y, x = selected_cell
                        num = int(event.unicode)
                        if valid(board, num, (y, x)):
                            board[y][x] = num
                            user_inputs[y][x] = True
                            if check_win(board):
                                game_won = True
                    elif event.key is pygame.K_BACKSPACE:
                        y, x = selected_cell
                        board[y][x] = 0
                        user_inputs[y][x] = False

        screen.fill(WHITE)
        draw_grid(board, user_inputs, selected_cell)
        if game_won:
            display_win_message()
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
