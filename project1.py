import pygame
import time
from collections import defaultdict

pygame.init()

WIDTH, HEIGHT = 680, 880
BOARD_SIZE = 8
SQUARE_SIZE = 80

LIGHT_SQUARE = (240, 217, 181)
DARK_SQUARE = (181, 136, 99)
HIGHLIGHT_COLOR = (247, 247, 105, 150)
SCOREBOARD_COLOR = (70, 70, 70)
WHITE_TEXT = (255, 255, 255)
BLACK_TEXT = (0, 0, 0)
WHITE_TIMER = (220, 245, 220)
BLACK_TIMER = (220, 220, 245)
TURN_HIGHLIGHT = (100, 200, 100)

# Symbol mapping (Unicode Chess Symbols)
SYMBOLS = {
    'r': '♜', 'n': '♞', 'b': '♝', 'q': '♛', 'k': '♚', 'p': '♟',
    'R': '♖', 'N': '♘', 'B': '♗', 'Q': '♕', 'K': '♔', 'P': '♙'
}

class Board:
    def __init__(self):
        self.grid = self.create_starting_board()
        self.move_history = []

    def create_starting_board(self):
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

    def move_piece(self, start, end):
        self.move_history.append({
            'start': start,
            'end': end,
            'captured': self.grid[end[0]][end[1]],
            'moved_piece': self.grid[start[0]][start[1]]
        })
        self.grid[end[0]][end[1]] = self.grid[start[0]][start[1]]
        self.grid[start[0]][start[1]] = ''

    def undo_move(self):
        if not self.move_history:
            return False
        last_move = self.move_history.pop()
        self.grid[last_move['start'][0]][last_move['start'][1]] = last_move['moved_piece']
        self.grid[last_move['end'][0]][last_move['end'][1]] = last_move['captured']
        return True

class ChessGame:
    def __init__(self):
        self.board = Board()
        self.current_player = 'white'
        self.scores = defaultdict(int)
        self.player_times = {'white': 600, 'black': 600}
        self.last_time_update = time.time()

    def update_timers(self):
        now = time.time()
        elapsed = now - self.last_time_update
        self.last_time_update = now
        if self.current_player == 'white':
            self.player_times['white'] = max(0, self.player_times['white'] - elapsed)
        else:
            self.player_times['black'] = max(0, self.player_times['black'] - elapsed)

    def is_valid_move(self, start, end):
        piece = self.board.grid[start[0]][start[1]]
        if not piece:
            return False
        if (self.current_player == 'white' and not piece.isupper()) or \
           (self.current_player == 'black' and piece.isupper()):
            return False
        target = self.board.grid[end[0]][end[1]]
        if target and ((piece.isupper() and target.isupper()) or (piece.islower() and target.islower())):
            return False
        if piece in ['P', 'p']:
            return self.is_valid_pawn_move(start, end)
        return True

    def is_valid_pawn_move(self, start, end):
        sr, sc = start
        er, ec = end
        piece = self.board.grid[sr][sc]
        direction = -1 if piece == 'P' else 1
        start_row = 6 if piece == 'P' else 1

        if sc == ec:
            if er == sr + direction and self.board.grid[er][ec] == '':
                return True
            if sr == start_row and er == sr + 2 * direction and \
               self.board.grid[sr + direction][ec] == '' and self.board.grid[er][ec] == '':
                return True
        elif abs(ec - sc) == 1 and er == sr + direction:
            if self.board.grid[er][ec] != '' and \
               ((piece == 'P' and self.board.grid[er][ec].islower()) or (piece == 'p' and self.board.grid[er][ec].isupper())):
                return True
        return False

    def make_move(self, start, end):
        if self.is_valid_move(start, end):
            target = self.board.grid[end[0]][end[1]]
            if target:
                self.scores[self.current_player] += self.get_piece_value(target)
            self.board.move_piece(start, end)
            self.current_player = 'black' if self.current_player == 'white' else 'white'
            self.update_timers()
            return True
        return False

    def undo_last_move(self):
        if self.board.undo_move():
            self.current_player = 'black' if self.current_player == 'white' else 'white'
            self.update_timers()
            return True
        return False

    def get_piece_value(self, piece):
        values = {'p': 1, 'P': 1, 'n': 3, 'N': 3, 'b': 3, 'B': 3, 'r': 5, 'R': 5, 'q': 9, 'Q': 9, 'k': 0, 'K': 0}
        return values.get(piece, 0)

    def format_time(self, sec):
        return f"{int(sec // 60)}:{int(sec % 60):02d}"

class ChessGUI:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Chess Game")
        self.font = pygame.font.SysFont('segoeuisymbol', 28)
        self.big_font = pygame.font.SysFont('segoeuisymbol', 48)
        self.timer_font = pygame.font.SysFont('segoeuisymbol', 32)
        self.button_font = pygame.font.SysFont('segoeuisymbol', 26)
        self.game = ChessGame()

    def draw_board(self):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                color = LIGHT_SQUARE if (row + col) % 2 == 0 else DARK_SQUARE
                pygame.draw.rect(self.screen, color, (20 + col*SQUARE_SIZE, 20 + row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                piece = self.game.board.grid[row][col]
                if piece:
                    symbol = SYMBOLS.get(piece, piece)
                    text_color = BLACK_TEXT if color == LIGHT_SQUARE else WHITE_TEXT
                    text = self.big_font.render(symbol, True, text_color)
                    rect = text.get_rect(center=(20 + col*SQUARE_SIZE + SQUARE_SIZE//2, 20 + row*SQUARE_SIZE + SQUARE_SIZE//2))
                    self.screen.blit(text, rect)

    def draw_scoreboard(self):
        pygame.draw.rect(self.screen, SCOREBOARD_COLOR, (0, HEIGHT-120, WIDTH, 120))
        w = WIDTH // 2 - 20
        pygame.draw.rect(self.screen, TURN_HIGHLIGHT if self.game.current_player == 'white' else (80, 80, 80), (20, HEIGHT-110, w, 50))
        pygame.draw.rect(self.screen, TURN_HIGHLIGHT if self.game.current_player == 'black' else (80, 80, 80), (WIDTH//2 + 10, HEIGHT-110, w, 50))

        self.screen.blit(self.font.render("WHITE", True, WHITE_TEXT), (40, HEIGHT-100))
        self.screen.blit(self.font.render("BLACK", True, WHITE_TEXT), (WIDTH//2 + 30, HEIGHT-100))
        self.screen.blit(self.font.render(f"Score: {self.game.scores['white']}", True, WHITE_TEXT), (40, HEIGHT-70))
        self.screen.blit(self.font.render(f"Score: {self.game.scores['black']}", True, WHITE_TEXT), (WIDTH//2 + 30, HEIGHT-70))

        white_time = self.timer_font.render(self.game.format_time(self.game.player_times['white']), True, WHITE_TIMER)
        black_time = self.timer_font.render(self.game.format_time(self.game.player_times['black']), True, BLACK_TIMER)
        self.screen.blit(white_time, (40, HEIGHT-40))
        self.screen.blit(black_time, (WIDTH//2 + 30, HEIGHT-40))

        pygame.draw.rect(self.screen, (100, 100, 100), (WIDTH//2 - 50, HEIGHT-30, 100, 30))
        self.screen.blit(self.button_font.render("UNDO", True, WHITE_TEXT), (WIDTH//2 - 30, HEIGHT-25))

    def get_square_from_pos(self, pos):
        x, y = pos
        if 20 <= x < 20 + BOARD_SIZE*SQUARE_SIZE and 20 <= y < 20 + BOARD_SIZE*SQUARE_SIZE:
            return (y - 20) // SQUARE_SIZE, (x - 20) // SQUARE_SIZE
        return None

    def is_undo_clicked(self, pos):
        x, y = pos
        return (WIDTH//2 - 50 <= x <= WIDTH//2 + 50) and (HEIGHT-30 <= y <= HEIGHT)

    def run(self):
        clock = pygame.time.Clock()
        running = True
        selected = None

        while running:
            self.game.update_timers()
            if self.game.player_times['white'] <= 0 or self.game.player_times['black'] <= 0:
                running = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if self.is_undo_clicked(pos):
                        self.game.undo_last_move()
                    else:
                        square = self.get_square_from_pos(pos)
                        if square:
                            if selected is None:
                                piece = self.game.board.grid[square[0]][square[1]]
                                if piece and ((self.game.current_player == 'white' and piece.isupper()) or
                                              (self.game.current_player == 'black' and piece.islower())):
                                    selected = square
                            else:
                                self.game.make_move(selected, square)
                                selected = None

            self.screen.fill((50, 50, 50))
            self.draw_board()
            self.draw_scoreboard()

            if selected:
                r, c = selected
                s = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE), pygame.SRCALPHA)
                s.fill(HIGHLIGHT_COLOR)
                self.screen.blit(s, (20 + c*SQUARE_SIZE, 20 + r*SQUARE_SIZE))

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    ChessGUI().run()
