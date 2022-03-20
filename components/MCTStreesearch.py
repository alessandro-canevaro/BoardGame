# MCTS algorithm about 2048
import random
import numpy as np
import math
from components.Board import Board
from components.Game_engine import GameEngine
import time
from multiprocessing.dummy import Pool as ThreadPool

possible_move = ['left', 'right', 'up', 'down']


class MCTSAgent:
    def __init__(self, board) -> None:
        self.board = board
        self.next_move = '',

    def GetNextMove(self) -> str:
        Simulation = MoveSimulation(self.board)
        empty_tiles = Simulation.board.GetEmptyTiles()
        max_number = np.max(Simulation.board.values)
        if max_number < 1024:
            if len(empty_tiles) > 7:
                Simulation.depth = 5  # 20
            elif len(empty_tiles) > 4 and max_number < 512:
                Simulation.depth = 15  # 60
            else:
                Simulation.depth = 20  # 160
        else:
            Simulation.depth = 50  # 200
        self.next_move = Simulation.BestNextMove()
        return self.next_move

    def UpdateBoard(self, current_board):
        self.board = current_board


class MoveSimulation:
    def __init__(self, board) -> None:
        self.board = board
        self.simulation_board = None
        self.max_score_move = 0
        self.depth = 20
        self.runs = 50

    def BestNextMove(self):
        # max_score = 0
        record_score = []
        Possible_move = self.board.PossibleMoves()
        for m in Possible_move:
            moved_board = Board(self.board)
            moved_board.Swipe(m, True)
            template_score = self.evalRandomRun(moved_board)
            record_score.append(template_score)
        # max_score = max(record_score)
        self.max_score_move = Possible_move[np.argmax(record_score)]
        # print(record_score)
        return self.max_score_move

    def evalRandomRun(self, board):
        total_score = 0
        i = 0
        move_depth = self.depth * 4 if self.depth < 45 else 100000
        for i in range(self.runs):
            simulation_board = Board(board)
            move = 0
            while simulation_board.PossibleMoves() and move < move_depth:
                simulation_board.Swipe(possible_move[math.floor(random.random() * 4)], False)
                move += 1
                position = simulation_board.GetEmptyTiles()
                if position:
                    rand_pos = random.sample(position, 1)
                    rand_num = random.choices([2, 4], [0.9, 0.1], k=1)
                    for pos, value in zip(rand_pos, rand_num):
                        simulation_board.SetEmptyTile(pos, value)
            simulation_score = int(np.sum(simulation_board.values))
            # total_score += simulation_board.score
            # max_score = int(np.max(simulation_board.values))
            total_score += simulation_score
            # simMax_num.append(max_score)
            # total_move += move
            i += 1
        sum_score = np.sum(total_score)
        # sum_move = np.sum(total_move)
        # simMax_score = max(simMax_num)
        return sum_score


def main():
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
    print("Do some tests...")
    max_number = []
    for j in range(20):
        max_num = main()
        max_number.append(max_num)
        j += 1
    print(max_number)
    print("All done")
