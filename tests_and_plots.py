#Main file from where the whole game is run

import matplotlib.pyplot as plt
from components.Board import Board
from components.Game_engine import GameEngine
from components.ExpectiMax import ExpectiMaxAgent

def ExpectiMaxTest(depth='adaptive', heuristic='snake', max_iter=10, goal=128, print_info=False):
    score_avg = []
    maxtile_stats = {}
    victory_stats = {'Victory': 0, 'Game Over':0}
    for i in range(max_iter):
        ge = GameEngine()
        ge.setRandomNumberInTile(k=2)
        em = ExpectiMaxAgent(ge.board, depth=depth, heuristic=heuristic)
        while True:
            """ for console based demostration of board game"""
            if print_info:
                ge.printBoard()

            if ge.isGameOver():
                isGameOver = True
                #print("Game over!")
                break
            elif ge.isGoal(goal=goal):
                isGameOver = False
                #print("Victory!")
                break

            em_move = em.ComputeNextMove()
            """ to display each move taken by agent """
            if print_info:
                print("Move: {}: Score: {} AI suggests: {}".format(i, int(ge.board.score), em_move))
            #move = ''
            #possible_moves = ge.board.PossibleMoves()
            #while move not in possible_moves:
            #    move = input("Select your next move {}:".format(possible_moves)).lower()
            #ge.board.Swipe(move, True)
            ge.board.Swipe(em_move, True)
            ge.setRandomNumberInTile(k=1)
            em.UpdateTree(ge.board, em_move)
        print("Match {} finished with {}. The score was: {}, and maximum tile was: {}".format(i, "Game over" if isGameOver else "Victory", ge.board.score, ge.board.GetMaxTileValue()))
        score_avg.append(ge.board.score)
        if ge.board.GetMaxTileValue() in maxtile_stats:
            maxtile_stats[ge.board.GetMaxTileValue()] += 1
        else:
            maxtile_stats[ge.board.GetMaxTileValue()] = 1
        victory_stats["Game Over" if isGameOver else "Victory"] += 1
    return sum(score_avg)/len(score_avg), maxtile_stats, victory_stats



if __name__ == "__main__":
    score_avg, maxtile_stats, victory_stats = ExpectiMaxTest(depth='adaptive', heuristic='snake8x', max_iter=17, goal=100000, print_info=False)
    print(score_avg, maxtile_stats, victory_stats)
    
    #plot max tile dict
    keys, items = zip(*sorted(maxtile_stats.items()))
    keys = [str(k) for k in keys]
    plt.figure(1)
    plt.bar(keys, items)

    #plot victory dict
    plt.figure(2)
    plt.bar(*zip(*victory_stats.items()))

    plt.show()


# ------- RESULTS --------

#ExpectiMaxTest(depth='adaptive', heuristic='snake', max_iter=50, goal=2048, print_info=False)
#time start = 9.40, time end = 11.15
#19518.72 {1024: 6, 2048: 43, 256: 1} {'Victory': 43, 'Game Over': 7}

#ExpectiMaxTest(depth=2, heuristic='snake', max_iter=50, goal=2048, print_info=False)
#time start = 10.25, time end = 12.00
#19081.68 {2048: 40, 1024: 8, 256: 1, 512: 1} {'Victory': 40, 'Game Over': 10}

#ExpectiMaxTest(depth=1, heuristic='snake', max_iter=50, goal=2048, print_info=False)
#time less than 1 min
#3326.96 {256: 24, 512: 10, 128: 11, 32: 1, 64: 4} {'Victory': 0, 'Game Over': 50}

#ExpectiMaxTest(depth='adaptive', heuristic='snake', max_iter=50, goal=100000, print_info=False)
#time start = 16.55, time end = 21.50
#52274.56 {4096: 25, 1024: 4, 2048: 19, 8192: 2} {'Victory': 0, 'Game Over': 50}

#ExpectiMaxTest(depth='adaptive', heuristic='snake8x', max_iter=50, goal=100000, print_info=False)
#time start = 12.20, time end = 23.00
"""
Match 0 finished with Game over. The score was: 36172, and maximum tile was: 2048
Match 1 finished with Game over. The score was: 80524, and maximum tile was: 4096
Match 2 finished with Game over. The score was: 57264, and maximum tile was: 4096
Match 3 finished with Game over. The score was: 32096, and maximum tile was: 2048
Match 4 finished with Game over. The score was: 32220, and maximum tile was: 2048
Match 5 finished with Game over. The score was: 36092, and maximum tile was: 2048
Match 6 finished with Game over. The score was: 68328, and maximum tile was: 4096
Match 7 finished with Game over. The score was: 67600, and maximum tile was: 4096
Match 8 finished with Game over. The score was: 67748, and maximum tile was: 4096
Match 9 finished with Game over. The score was: 119312, and maximum tile was: 8192
Match 10 finished with Game over. The score was: 36604, and maximum tile was: 2048
Match 11 finished with Game over. The score was: 67864, and maximum tile was: 4096
Match 12 finished with Game over. The score was: 50620, and maximum tile was: 4096
Match 13 finished with Game over. The score was: 51896, and maximum tile was: 4096
Match 14 finished with Game over. The score was: 16352, and maximum tile was: 1024
Match 15 finished with Game over. The score was: 27180, and maximum tile was: 2048
Match 16 finished with Game over. The score was: 31428, and maximum tile was: 2048
Match 17 finished with Game over. The score was: 32616, and maximum tile was: 2048
Match 18 finished with Game over. The score was: 79756, and maximum tile was: 4096
Match 19 finished with Game over. The score was: 59404, and maximum tile was: 4096
Match 20 finished with Game over. The score was: 61228, and maximum tile was: 4096
Match 21 finished with Game over. The score was: 16940, and maximum tile was: 1024
Match 22 finished with Game over. The score was: 60932, and maximum tile was: 4096
Match 23 finished with Game over. The score was: 50720, and maximum tile was: 4096
Match 24 finished with Game over. The score was: 54440, and maximum tile was: 4096
Match 25 finished with Game over. The score was: 78348, and maximum tile was: 4096
Match 26 finished with Game over. The score was: 29764, and maximum tile was: 2048
Match 27 finished with Game over. The score was: 16104, and maximum tile was: 1024
Match 28 finished with Game over. The score was: 61188, and maximum tile was: 4096
Match 29 finished with Game over. The score was: 36216, and maximum tile was: 2048
Match 30 finished with Game over. The score was: 61336, and maximum tile was: 4096
Match 31 finished with Game over. The score was: 70788, and maximum tile was: 4096
Match 32 finished with Game over. The score was: 16392, and maximum tile was: 1024

Match 0 finished with Game over. The score was: 61632, and maximum tile was: 4096
Match 1 finished with Game over. The score was: 28216, and maximum tile was: 2048
Match 2 finished with Game over. The score was: 36116, and maximum tile was: 2048
Match 3 finished with Game over. The score was: 42912, and maximum tile was: 2048
Match 4 finished with Game over. The score was: 56780, and maximum tile was: 4096
Match 5 finished with Game over. The score was: 34548, and maximum tile was: 2048
Match 6 finished with Game over. The score was: 30552, and maximum tile was: 2048
Match 7 finished with Game over. The score was: 133180, and maximum tile was: 8192
Match 8 finished with Game over. The score was: 58972, and maximum tile was: 4096
Match 9 finished with Game over. The score was: 27520, and maximum tile was: 2048
Match 10 finished with Game over. The score was: 72420, and maximum tile was: 4096

Match 11 finished with Game over. The score was: 80212, and maximum tile was: 4096
Match 12 finished with Game over. The score was: 36176, and maximum tile was: 2048
Match 13 finished with Game over. The score was: 35996, and maximum tile was: 2048
Match 14 finished with Game over. The score was: 53620, and maximum tile was: 4096
Match 15 finished with Game over. The score was: 71640, and maximum tile was: 4096
Match 16 finished with Game over. The score was: 56428, and maximum tile was: 4096
"""

#[36172, 80524, 57264, 32096, 32220, 36092, 68328, 67600, 67748, 119312, 36604, 67864, 50620, 51896, 16352, 27180, 31428, 32616, 79756, 59404, 61228, 16940, 60932, 50720, 54440, 78348, 29764, 16104, 61188, 36216, 61336, 70788, 16392, 61632, 28216, 36116, 42912, 56780, 34548, 30552, 133180, 58972, 27520, 72420, 80212, 36176, 35996, 53620, 71640, 56428]



