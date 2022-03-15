
import pygame
from pygame.locals import *
from components.Game_engine import GameEngine
from components.Board import Board
from components.ExpectiMax import ExpectiMaxAgent

board_size = 4

TILE_COLOR = {2: "#EDE4DA", 4: "#EDDFC9",  8: "#F2B178", 16: "#F59563", 32: "#F67C5F", 64: "#F65D3B",
              128: "#EDCF72", 256: "#EECC61", 512: "#EDC751", 1024: "#EEC43F", 2048: "#edc22e", 4096: "#3c3a32"}

FONT_COLOR = {2: "#766E65", 4: "#766E65", 8: "#F8F6F2", 16: "#F8F6F2", 32: "#F8F6F2", 64: "#F8F6F2",
              128: "#F8F6F2", 256: "#F8F6F2", 512: "#F8F6F2", 1024: "#F8F6F2", 2048: "#F8F6F2", 4096: "#F8F6F2"}
BG_COLOR = '#BBAD9F'
NV_COLOR = '#CCC1B4'


class GuiClass():
    def __init__(self) -> None:
        self.game_engine = GameEngine()
        self.screen_w = 400
        self.screen_h = self.screen_w
        self.tile_gap = 10
        pygame.init()
        pygame.display.set_caption("AI-BoardGame 2048")
        pygame.font.init()
        self.primary_font = pygame.font.SysFont('Comic Sans MS', 36)
        self.screen = pygame.display.set_mode((self.screen_w, self.screen_h))

    def auto_play(self):
            #clock = pygame.time.Clock()
            self.draw_game()
            while pygame.event.get():
                self.draw_game()
                pygame.display.flip()

            """while True:
                self.draw_game()
                pygame.display.flip()
                cmd = key_press()
                if cmd == 'l':
                    board = self.swipe_left(self.board)
                    self.board = board
                elif cmd == 'q':
                    break"""

    """ Graphicl representation of the game """
    def draw_game(self):
        self.screen.fill(BG_COLOR)

        for i in range(board_size):
            for j in range(board_size):
                temp = self.game_engine.board.values[i][j]
                top_left_x = j * self.screen_w // board_size + self.tile_gap
                top_left_y = i * self.screen_h // board_size + self.tile_gap
                tile_w = self.screen_w // board_size - 2 * self.tile_gap
                tile_h = self.screen_h // board_size - 2 * self.tile_gap

                if temp == 0:
                    pygame.draw.rect(self.screen, NV_COLOR,
                                    pygame.Rect(top_left_x, top_left_y, tile_w, tile_h))
                    pygame.display.flip()
                    # continue
                elif temp > 2048:
                    pygame.draw.rect()
                    pygame.draw.rect(self.screen, TILE_COLOR[4096],
                                    pygame.Rect(top_left_x, top_left_y, tile_w, tile_h))
                    text = self.primary_font.render(
                        f'{temp}', True, FONT_COLOR[4096])
                    text_pos = text.get_rect(
                        center=(top_left_x + tile_w / 2, top_left_y + tile_h / 2))
                    self.screen.blit(text, text_pos)
                    pygame.display.flip()

                else:
                    pygame.draw.rect(self.screen, TILE_COLOR[temp],
                                    pygame.Rect(top_left_x, top_left_y, tile_w, tile_h))
                    text = self.primary_font.render(
                        f'{temp}', True, FONT_COLOR[2])
                    text_pos = text.get_rect(
                        center=(top_left_x + tile_w / 2, top_left_y + tile_h / 2))
                    self.screen.blit(text, text_pos)
                    pygame.display.flip()


    def key_press(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return 'q'
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        return 'u'
                    elif event.key == K_RIGHT:
                        return 'r'
                    elif event.key == K_LEFT:
                        return 'l'
                    elif event.key == K_DOWN:
                        return 'd'
                    elif event.key == K_q or event.key == K_ESCAPE:
                        return 'q'
    

if __name__ == '__main__':
    gc = GuiClass()
    gc.game_engine.setRandomNumberInTile(k=2)
    em = ExpectiMaxAgent(gc.game_engine.board, heuristic='snake')
    i = 0
    while i <= 10000:
        """ for console based demostration of board game"""
        gc.game_engine.printBoard()
        """ for graphical demostration of board game"""
        gc.auto_play()
    
        if gc.game_engine.isGameOver():
            print("Game over!")
            break
        #elif ge.isGoal():
        #    print("Victory!")
        #    break

        em_move = em.ComputeNextMove()
        """ to display each move taken by agent """
        print("Move: {}: Score: {} AI suggests: {}".format(i, int(gc.game_engine.board.score), em_move))
        #move = ''
        #possible_moves = ge.board.PossibleMoves()
        #while move not in possible_moves:
        #    move = input("Select your next move {}:".format(possible_moves)).lower()
        #ge.board.Swipe(move, True)
        gc.game_engine.board.Swipe(em_move, True)
        gc.game_engine.setRandomNumberInTile(k=1)
        em.UpdateTree(gc.game_engine.board, em_move)
        i += 1
    