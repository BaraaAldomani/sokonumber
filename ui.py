import pygame
import pyfiglet
import termcolor
from edit_image import EditImage

class Ui:
    def __init__(self , board , win):
        self.board = board
        self.win = win


    wall = pygame.image.load('images/wall.png')
    floor = pygame.image.load('images/floor.png')
    box = pygame.image.load('images/box.png')
    background = (255, 255, 155)
    edit = EditImage()

    
    def get_screen(self):
        size = self.size_screen()
        screen = pygame.display.set_mode(size)
        return screen


    @staticmethod
    def print_win_text(text):
        print()
        print(termcolor.colored(pyfiglet.figlet_format(text , font='alligator'),'green'))
        print()
        
    @staticmethod
    def print_values(mode:str , track:int, visited:int , time:int):
        print()
        print( mode, 'visited:' , termcolor.colored(str(visited),'green'))
        print( mode, 'track:' , termcolor.colored(str(track),'green'))
        print( mode, 'time:' , termcolor.colored(str(time),'green'))
    @staticmethod
    def print_movment(mode:str,color:str ,track:int):
        print(mode, 'Movment: ',termcolor.colored(str(track) , color))
    def size_screen(self):
        x = 0
        y = len(self.board)

        for line in self.board:
            if (len(line) > x):
                x = len(line)
        return (x*64, (y * 64))

    @staticmethod
    def print_board(node):
        for row in node:
            print(row)
        print()



    
    def print_game(self,board):
        screen = self.get_screen()
        screen.fill(self.background)

        x = 0
        y = 0
        for i in range(len(self.win)):
            for j in range(len(self.win[i])):
                if (self.win[i][j] == ' '):
                    screen.blit(self.floor, (x, y))
                elif (self.win[i][j] == '#'):
                    screen.blit(self.wall, (x, y))
                else:
                    screen.blit(self.edit.add_goal_image(
                        int(self.win[i][j])), (x, y))

                if (board[i][j] not in ['#', ' ']):
                    screen.blit(self.edit.add_box_image(
                        int((board[i][j]))), (x, y))
                if (board[i][j] == self.win[i][j] and board[i][j] not in ['#', ' ']):
                    screen.blit(self.edit.add_done_image(
                        int((board[i][j]))), (x, y))
                x += 64
            x = 0
            y += 64
