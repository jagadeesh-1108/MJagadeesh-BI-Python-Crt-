import pygame
import sys
import time

pygame.init()

# --- Constants ---
WIDTH, HEIGHT = 640, 640
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS
WHITE = (240, 217, 181)
BROWN = (181, 136, 99)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
TEXT_COLOR = (255, 255, 255)  # <-- White color for text

# Setup screen and font
screen = pygame.display.set_mode((WIDTH, HEIGHT + 100))
pygame.display.set_caption("Full Chess Game")
FONT = pygame.font.SysFont("segoeuisymbol", 36)

# Piece symbols (Unicode)
symbols = {
    'P': '♙', 'R': '♖', 'N': '♘', 'B': '♗', 'Q': '♕', 'K': '♔',
    'p': '♟', 'r': '♜', 'n': '♞', 'b': '♝', 'q': '♛', 'k': '♚'
}

# Initialize board
def init_board():
    return [
        ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
        ['p'] * 8,
        [''] * 8,
        [''] * 8,
        [''] * 8,
        [''] * 8,
        ['P'] * 8,
        ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
    ]

board = init_board()
selected = None
valid_moves = []
turn = 'white'
game_over = False
start_time_white = time.time()
start_time_black = time.time()
white_time = 300  # 5 minutes
black_time = 300

# Scoring
white_score = 0
black_score = 0
piece_values = {'p': 1, 'n': 3, 'b': 3, 'r': 5, 'q': 9, 'k': 0}
white_captures = []
black_captures = []

# --- Helper Functions ---
def piece_color(piece):
    return 'white' if piece.isupper() else 'black' if piece else None

def is_inside(r, c):
    return 0 <= r < 8 and 0 <= c < 8

def get_moves(r, c):
    piece = board[r][c]
    color = piece_color(piece)
    moves = []

    directions = {
        'P': [(-1, 0)], 'p': [(1, 0)],
        'R': [(1,0), (-1,0), (0,1), (0,-1)],
        'N': [(-2,-1), (-2,1), (-1,-2), (-1,2), (1,-2), (1,2), (2,-1), (2,1)],
        'B': [(1,1), (-1,1), (1,-1), (-1,-1)],
        'Q': [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,1), (1,-1), (-1,-1)],
        'K': [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,1), (1,-1), (-1,-1)]
    }

    if piece.upper() == 'P':
        dir = -1 if piece.isupper() else 1
        start_row = 6 if piece.isupper() else 1

        if is_inside(r + dir, c) and board[r + dir][c] == '':
            moves.append((r + dir, c))
            if r == start_row and board[r + 2 * dir][c] == '':
                moves.append((r + 2 * dir, c))

        for dc in [-1, 1]:
            if is_inside(r + dir, c + dc):
                target = board[r + dir][c + dc]
                if target and piece_color(target) != color:
                    moves.append((r + dir, c + dc))

    else:
        for dr, dc in directions.get(piece.upper(), []):
            for i in range(1, 8):
                nr, nc = r + dr * i, c + dc * i
                if not is_inside(nr, nc): break
                target = board[nr][nc]
                if target == '':
                    moves.append((nr, nc))
                elif piece_color(target) != color:
                    moves.append((nr, nc))
                    break
                else:
                    break
                if piece.upper() in ['N', 'K']: break

    return moves

def draw_board():
    for r in range(8):
        for c in range(8):
            color = WHITE if (r + c) % 2 == 0 else BROWN
            pygame.draw.rect(screen, color, (c*SQUARE_SIZE, r*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            if selected and (r, c) in valid_moves:
                pygame.draw.rect(screen, GREEN, (c*SQUARE_SIZE, r*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 3)
            if board[r][c]:
                text = FONT.render(symbols[board[r][c]], True, BLACK)
                screen.blit(text, (c*SQUARE_SIZE + 10, r*SQUARE_SIZE + 5))

def draw_timer():
    global white_time, black_time, start_time_white, start_time_black

    if turn == 'white':
        white_time -= time.time() - start_time_white
        start_time_white = time.time()
    else:
        black_time -= time.time() - start_time_black
        start_time_black = time.time()

    white_timer_text = FONT.render(f"White: {int(white_time)}s", True, TEXT_COLOR)
    black_timer_text = FONT.render(f"Black: {int(black_time)}s", True, TEXT_COLOR)
    screen.blit(white_timer_text, (10, HEIGHT + 10))
    screen.blit(black_timer_text, (10, HEIGHT + 50))

def draw_score():
    white_score_text = FONT.render(f"Score: {white_score}", True, TEXT_COLOR)
    black_score_text = FONT.render(f"Score: {black_score}", True, TEXT_COLOR)
    screen.blit(white_score_text, (WIDTH - 150, HEIGHT + 10))
    screen.blit(black_score_text, (WIDTH - 150, HEIGHT + 50))

    white_caps_text = ''.join([symbols[p] for p in white_captures])
    black_caps_text = ''.join([symbols[p] for p in black_captures])

    white_caps_render = FONT.render(f"🗡 {white_caps_text}", True, TEXT_COLOR)
    black_caps_render = FONT.render(f"🗡 {black_caps_text}", True, TEXT_COLOR)

    screen.blit(white_caps_render, (WIDTH//2 - 60, HEIGHT + 10))
    screen.blit(black_caps_render, (WIDTH//2 - 60, HEIGHT + 50))

def move_piece(sr, sc, dr, dc):
    global turn, white_score, black_score
    captured = board[dr][dc]
    board[dr][dc] = board[sr][sc]
    board[sr][sc] = ''

    if captured:
        if piece_color(captured) == 'white':
            black_score += piece_values[captured.lower()]
            black_captures.append(captured)
        else:
            white_score += piece_values[captured.lower()]
            white_captures.append(captured)

    turn = 'black' if turn == 'white' else 'white'

def handle_click(pos):
    global selected, valid_moves
    x, y = pos[0] // SQUARE_SIZE, pos[1] // SQUARE_SIZE
    if y >= 8: return
    piece = board[y][x]
    if selected:
        if (y, x) in valid_moves:
            move_piece(selected[0], selected[1], y, x)
        selected = None
        valid_moves = []
    elif piece and piece_color(piece) == turn:
        selected = (y, x)
        valid_moves = get_moves(y, x)

# --- Main Loop ---
clock = pygame.time.Clock()
while True:
    screen.fill((0, 0, 0))
    draw_board()
    draw_timer()
    draw_score()
    pygame.display.update()
    clock.tick(60)

    if white_time <= 0 or black_time <= 0:
        winner = "Black" if white_time <= 0 else "White"
        print(f"{winner} wins on time!")
        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            handle_click(pygame.mouse.get_pos())