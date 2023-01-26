# import pygame

# pygame.init()


# class Button:
#     """Create a button, then blit the surface in the while loop"""

#     def __init__(self, x, y,):
#         self.x = x
#         self.y = y

#     def get_next_level(self, text,):
#         self.surface.blit(text, (0, 0))
#         self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

#     def click(self, event, callback):
#         self.x, self.y = pygame.mouse.get_pos()
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             if pygame.mouse.get_pressed()[0]:
#                 if self.rect.collidepoint(self.x, self.y):
#                     callback()
