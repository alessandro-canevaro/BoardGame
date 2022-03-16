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
    score_avg, maxtile_stats, victory_stats = ExpectiMaxTest(depth=1, heuristic='snake', max_iter=10, goal=256, print_info=False)
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

#do stuff...