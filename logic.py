import sys

import pygame
from node import Node
from structure import Game
import queue as Queue
import time
import copy
from ui import Ui

class Logic:
    def __init__(self, level) -> None:
        self.game = Game(level)
        self.ui = Ui(self.game.board.value, self.game.win)
        self.screen = self.ui.get_screen()

    def userPlay(self):
        while True:
            self.ui.print_game(self.game.board.value)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.game.move('up', self.game.board.value)
                    if event.key == pygame.K_DOWN:
                        self.game.move('down', self.game.board.value)
                    if event.key == pygame.K_LEFT:
                        self.game.move('left', self.game.board.value)
                    if event.key == pygame.K_RIGHT:
                        self.game.move('right', self.game.board.value)
                    elif event.key == pygame.K_q:
                        sys.exit(0)
                    self.game.track.append(self.game.board)
                    if (self.game.is_final_state(self.game.board)):
                        self.ui.print_win_text('w i n')
                        self.ui.print_movment('User play','green' ,len(self.game.track))
                pygame.display.update()

    def DFS(self, node: Node):
        now = time.time()
        stack = Queue.LifoQueue()
        stack.put(node)
        self.game.visited.append((node))
        while stack:
            node = stack.get()
            self.ui.print_game(node.value)
            for state in self.game.get_next_states(node):
                self.game.is_end_game(state,node,now)
                if (not self.game.check_if_in_visited((state))):
                    stack.put(state)
                    self.game.visited.append((state))
                pygame.display.update()

    def BFS(self, node: Node):
        now = time.time()
        queue = Queue.Queue()
        queue.put(node)
        self.game.visited.append((node))
        while queue:
            node = queue.get()
            self.ui.print_game(node.value)
            for state in self.game.get_next_states(node):
                self.game.is_end_game(state,node,now)
                if (not self.game.check_if_in_visited((state))):
                    queue.put(state)
                    self.game.visited.append((state))
                pygame.display.update()

    def UCS(self, node: Node):
        now = time.time()
        queue = Queue.PriorityQueue()
        queue.put((node.cost, node))
        self.game.visited.append(node)
        while queue:
            temp_node = queue.queue.pop(0)
            self.ui.print_game(temp_node[1].value)  
            for state in self.game.get_next_states(temp_node[1]):
                self.game.is_end_game(state,temp_node[1],now)
                if (not self.game.check_if_in_visited(state)):
                    queue.put((state.depth, state))
                    self.game.visited.append(state)
                pygame.display.update()

    def AStar(self,node :Node):
        now = time.time()
        queue = Queue.PriorityQueue()
        queue.put(node)
        while queue:
            temp_node = queue.queue.pop(0)
            if (not self.game.check_if_in_visited(temp_node)):
                self.game.visited.append(temp_node)
                # self.ui.print_game(temp_node.value)  
                for state in self.game.get_next_states(temp_node):
                    self.game.is_end_game(temp_node,now)
                    queue.put(state)
                    pygame.display.update()
