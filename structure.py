
import sys
import levels.levels as levels
import pygame
import copy
from node import Node
import collections
from ui import Ui
import numpy as nb
import time

sys.setrecursionlimit(100000)


class Game:

    def __init__(self, level):

        if level == 1:
            self.board = Node(levels.level1)
            self.win = levels.level1_win
        elif level == 2:
            self.board = Node(levels.level2)
            self.win = levels.level2_win
        elif level == 3:
            self.board = Node(levels.level3)
            self.win = levels.level3_win
        elif level == 4:
            self.board = Node(levels.level4)
            self.win = levels.level4_win
        elif level == 5:
            self.board = Node(levels.level5)
            self.win = levels.level5_win
        elif level == 6:
            self.board = Node(levels.level6)
            self.win = nb.array(levels.level6_win)

    visited = []
    track = []
    done = False

    def move(self, dir, board):
        if (dir == 'right'):
            self.move_right(board)
        elif (dir == 'left'):
            self.move_left(board)
        elif (dir == 'up'):
            self.move_up(board)
        elif (dir == 'down'):
            self.move_down(board)
        return board

    def move_right(self, board):
        pre = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if (board[i][j] not in ['#', ' ']):
                    if (board[i][j+1] == ' '):
                        if (pre.__contains__(board[i][j])):
                            continue
                        temp = board[i][j]
                        board[i][j] = board[i][j+1]
                        board[i][j+1] = temp
                        pre.append(temp)

    def move_left(self, board):
        pre = []
        next = ''
        for i in range(len(board)):
            for j in range(len(board[i])):
                if (board[i][j] not in ['#', ' ']):
                    if (board[i][j-1] == ' '):
                        if (pre.__contains__(board[i][j]) or next == board[i][j-2]):
                            continue
                        temp = board[i][j]
                        board[i][j] = board[i][j-1]
                        next = temp
                        board[i][j-1] = temp
                        pre.append(temp)

    def move_up(self, board):
        pre = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if (board[i][j] not in ['#', ' ']):
                    if (pre.__contains__(board[i - 2][j])):

                        continue
                    elif (board[i-1][j] == ' '):

                        temp = board[i][j]
                        board[i][j] = board[i-1][j]
                        board[i-1][j] = temp
                        pre.append(temp)

    def move_down(self, board):
        pre = []
        for i in range(len(board)):
            for j in range(len(board[i]),):
                if (board[i][j] not in ['#', ' ']):
                    if (board[i+1][j] == ' '):
                        if (pre.__contains__(board[i][j])):
                            continue
                        else:
                            temp = board[i][j]
                            board[i][j] = board[i+1][j]
                            board[i+1][j] = temp
                            pre.append(temp)

    def check_move(self, node):
        directions = ['up',  'down', 'right', 'left']
        possible_directions = []
        for dir in directions:
            temp_node = copy.deepcopy(node)
            temp = self.move(dir, temp_node.value)
            if (not self.equal(temp, node.value)):
                possible_directions.append(dir)
        return possible_directions

    def get_pos(self, board):
        boxs_pos = dict()
        goals_pos = dict()
        for i in range(len(board)):
            for j in range(len(board[i])):
                if (self.win[i][j] not in ['#', ' ']):
                    goals_pos[int(self.win[i][j])] = [i, j]
                if (board[i][j] not in ['#', ' ']):
                    boxs_pos[int(board[i][j])] = [i, j]

        return boxs_pos, goals_pos

    def heuristic_cutom(self, board ,  cost):
        pos = self.get_pos(board)
        boxs = dict(sorted(pos[0].items()))
        goals = dict(sorted(pos[1].items()))
        
        for i in boxs:
            if(boxs[i] == goals[i]):
                cost+=1
        return abs(cost - len(boxs))

    def heuristic_manhatin(self, board , cost):
        pos = self.get_pos(board)
        boxs = dict(sorted(pos[0].items()))
        goals = dict(sorted(pos[1].items()))
        cost = 0
        for i in boxs:
            cost += abs(boxs[i][0] - goals[i][0]) + abs(boxs[i][1] - goals[i][1])
        return cost

    def get_next_states(self, node: Node):
        cost =self.heuristic_cutom(node.value , node.cost)
        next_states = []
        possible_directions = self.check_move(node)
        for dir in possible_directions:
            temp_node = copy.deepcopy(node)
            state = self.move(dir, temp_node.value)
            next_node = Node(state, node, node.depth , cost)
            next_states.append(next_node)

        return next_states

    def equal(self, temp_node, node):
        for i in range(len(temp_node)):
            for j in range(len(temp_node[i])):
                
                if (temp_node[i][j] != node[i][j]):
                    return False
        return True

    def check_if_in_visited(self, node: Node):
        for state in self.visited:
            if (self.equal(state.value, node.value)):
                
                return True
        return False

    def is_final_state(self, node: Node):
        if (self.equal(node.value,self.win)):
            
            return True
        return False
    
    def show_soluation(self, track , ui:Ui):
        temp = track[::-1]
        node = 0
        while True:
            if (node == len(temp)):
                return
            for event in pygame.event.get():
                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_SPACE):
                        ui.print_game(temp[node].value)

                        pygame.display.update()
                        node += 1
                if event.type == pygame.QUIT:
                    sys.exit(0)

    def is_end_game(self , end_node:Node , time_now):
        if (self.is_final_state(end_node)):
            ui  = Ui(end_node.value,self.win)
            self.visited.append((end_node))
            temp_now = time.time()
            
            self.get_track(end_node)
                    
            ui.print_game(end_node.value)
            pygame.display.update()
            Ui.print_values('A Star', len(self.track), len(
                self.visited), round(temp_now - time_now, 2))
            Ui.print_win_text('w i n')
            self.show_soluation(self.track , ui)
            Ui.print_win_text('^ _ ^')
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit(0)
                
    def get_track(self,state:Node):
        temp = copy.deepcopy(state)
        while True:
            if (temp.father == None):
                self.track.append(temp)
                break
            elif (temp.father != None):
                self.track.append(temp)
                temp = temp.father