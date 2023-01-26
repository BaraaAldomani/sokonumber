from PIL import Image, ImageDraw
import pygame
class EditImage:
    def add_box_image(self, number):
        img = Image.open("images/box.png")
        draw = ImageDraw.Draw(img)
        draw.text((28, 28), f"{number}", (255, 255, 255))
        img.save(f'images/box{number}.png')
        return pygame.image.load(f'images/box{number}.png')

    def add_done_image(self, number):
        img = Image.open("images/box.png")
        draw = ImageDraw.Draw(img)
        draw.text((28, 28), f"{number}", (0, 255, 0))
        img.save(f'images/box_done{number}.png')
        return pygame.image.load(f'images/box_done{number}.png')

    def add_goal_image(self, number):
        img = Image.open("images/floor.png")
        draw = ImageDraw.Draw(img)
        draw.text((28, 28), f"{number}", (100, 100, 100))
        img.save(f'images/goal{number}.png')
        return pygame.image.load(f'images/goal{number}.png')