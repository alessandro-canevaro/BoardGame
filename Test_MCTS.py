# Main file from where the whole game is run

import matplotlib.pyplot as plt
from components.Board import Board
import numpy as np
from collections import Counter
from components.Game_engine import GameEngine
from components.MCTStreesearch import MCTSAgent


def MCTSTest():
    ge = GameEngine()
    ge.setRandomNumberInTile(k=2)
    mc = MCTSAgent(ge.board)
    i = 0
    for i in range(10000):
        # ge.printBoard()
        # empty_tiles = ge.board.GetEmptyTiles()
        if ge.isGameOver():
            print("Game over!")
            return np.max(ge.board.values)
        if ge.isGoal():
            print("victory")
            return np.max(ge.board.values)
        mc_move = mc.GetNextMove()
        print("Move: {}: Score: {} AI suggests: {}".format(i, int(ge.board.score), mc_move))
        ge.board.Swipe(mc_move, True)
        ge.setRandomNumberInTile(k=1)
        mc.UpdateBoard(ge.board)
        i += 1

if __name__ == "__main__":
    max_number = []
    max_iter = 20
    for j in range(max_iter):
        max_num = MCTSTest()
        max_number.append(max_num)
        j += 1
    result = Counter(max_number)
    keys, items = zip(*sorted(result.items()))
    keys = [str(k) for k in keys]
    plt.figure(1)
    plt.bar(keys, items)
    # plt.bar(range(len(result)), result)
    plt.show()

# ------- RESULTS --------

# MCTSTest(max_iter=20, goal=2048, move_depth = depth * 2)
# time start = 18.00, time end = 22.30
# {1024: 16, 2048: 2, 256: 1, 512:1} {'Victory': 2, 'Game Over': 18}

# MCTSTest(max_iter=20, goal=2048, move_depth = depth * 1)
# time start = 8.00, time end = 10.00
# {256: 1, 512: 6, 1024: 13} {'Victory': 0, 'Game Over': 20}

# MCTSTest(max_iter=20, goal=2048, move_depth = depth * 4)
# time start = 10.30, time end = 17.30
# {1024: 7, 2048: 11, 512: 2} {'Victory': 11, 'Game Over': 9}

