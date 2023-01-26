

from logic import Logic
from structure import Game


def main():
    print('1 ) User play')
    print('2 ) DFS Methode')
    print('3 ) BFS Methode')
    print('4 ) UCS Methode')
    print('5 ) AStar Methode')

    user_input = input('choose mode play:\n')
    lvl = int(input('choose level:\n'))

    game = Game(lvl)
    logic = Logic(lvl)
    if (user_input == '1'):
        logic.userPlay()
    elif (user_input == '2'):
        logic.DFS(game.board)
    elif (user_input == '3'):
        logic.BFS(game.board)
    elif (user_input == '4'):
        logic.UCS(game.board)
    elif (user_input == '5'):
        logic.AStar(game.board)


main()
