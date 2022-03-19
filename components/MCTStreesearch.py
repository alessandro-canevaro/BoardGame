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
            if len(empty_tiles) > 7 :
                Simulation.runs = 5  # 20
            elif len(empty_tiles) > 4 and max_number < 512:
                Simulation.runs = 15  # 40
            else:
                Simulation.runs = 20
        else:
            Simulation.runs = 35  # 70
        self.next_move = Simulation.BestNextMove()
        if any(1024 in row for row in Simulation.board):
            print(Simulation.runs)
        return self.next_move

    def UpdateBoard(self, current_board):
        self.board = current_board


class MoveSimulation:
    def __init__(self, board) -> None:
        self.board = board
        self.simulation_board = None
        self.max_score_move = 0
        self.runs = 15

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
        print(record_score)
        return self.max_score_move

    def evalRandomRun(self, board):
        total_score = 0
        # simMax_num = []
        # total_move = 0
        i = 0
        move_depth = self.runs * 4
        for i in range(self.runs):
            simulation_board = Board(board)
            # Possible_move = simulation_board.PossibleMoves()
            move = 0
            while simulation_board.PossibleMoves() and move < move_depth:
                simulation_board.Swipe(possible_move[math.floor(random.random() * 4)], True)
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
        avg_score = sum_score / self.runs
        # simMax_score = max(simMax_num)
        return sum_score
        # return avg_score


def main():
    ge = GameEngine()
    ge.setRandomNumberInTile(k=2)
    mc = MCTSAgent(ge.board)
    i = 0
    while i <= 10000:
        ge.printBoard()
        if ge.isGameOver():
            print("Game over!")
            break
        if ge.isGoal():
            print("victory")
            break
        # empty_tiles = ge.board.GetEmptyTiles()
        mc_move = mc.GetNextMove()
        print("Move: {}: Score: {} AI suggests: {}".format(i, int(ge.board.score), mc_move))
        ge.board.Swipe(mc_move, True)
        ge.setRandomNumberInTile(k=1)
        mc.UpdateBoard(ge.board)
        i += 1


if __name__ == "__main__":
    print("Do some tests...")
    # b = Board()
    # b.SetEmptyTile((2, 2), 2)
    # print(b)
    # agent = MCTSAgent(b, 'debug')
    # print(agent.board)
    main()
    print("All done")
