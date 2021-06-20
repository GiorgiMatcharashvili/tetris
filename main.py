import pygame
import time
from random import choice
from random import randint

class Shape:
    def __init__(self,color, coordinates_list):
        self.color = color
        self.coordinates_list = coordinates_list

        self.draw()

    def draw(self):
        for coordinates in self.coordinates_list:
            color_box(coordinates, self.color)

    def erase(self):
        for coordinates in self.coordinates_list:
            color_box(coordinates, background_colour)

    def check(self,coordinates_list):
        for each in coordinates_list:
            x = each[0]
            y = each[1]

            if x in range(0,10) and y in range(0, 20):
                continue
            else:
                return False
        return True

    def is_at_bottom(self):
        global bottom_boxs
        for each in self.coordinates_list:
            if each in bottom_boxs:
                return True
        return False

    def add_at_bottom(self):
        global bottom_boxs
        for each in self.coordinates_list:
            bottom_boxs.add(each)
            each = (each[0], each[1] - 1)
            bottom_boxs.add(each)


class O(Shape):
    def __init__(self, x, y, color):
        occupied_coordinates = [(x,y),(x,y-1),(x+1,y-1),(x+1,y)]

        if self.check(occupied_coordinates):
            super().__init__(color, occupied_coordinates)
            self.occupied_coordinates = occupied_coordinates


    def move(self, x="", y=""):
        if x == "":x = self.occupied_coordinates[0][0]
        if y == "":y = self.occupied_coordinates[0][1]

        occupied_coordinates = [(x, y), (x, y - 1), (x + 1, y - 1), (x + 1, y)]

        if self.check(occupied_coordinates):
            self.erase()
            super().__init__(self.color, occupied_coordinates)
            self.occupied_coordinates = occupied_coordinates

class I(Shape):
    def __init__(self, x, y, color):
        occupied_coordinates = [(x,y),(x,y-1),(x,y-2),(x,y-3)]

        if self.check(occupied_coordinates):
            super().__init__(color, occupied_coordinates)
            self.occupied_coordinates = occupied_coordinates

    def move(self, x="", y=""):
        if x == "": x = self.occupied_coordinates[0][0]
        if y == "": y = self.occupied_coordinates[0][1]

        occupied_coordinates = [(x,y),(x,y-1),(x,y-2),(x,y-3)]

        if self.check(occupied_coordinates):
            self.erase()
            super().__init__(self.color, occupied_coordinates)
            self.occupied_coordinates = occupied_coordinates

class S(Shape):
    def __init__(self, x, y, color):
        occupied_coordinates = [(x,y),(x+1,y),(x+1,y-1),(x+2,y-1)]

        if self.check(occupied_coordinates):
            super().__init__(color, occupied_coordinates)
            self.occupied_coordinates = occupied_coordinates

    def move(self, x="", y=""):
        if x == "": x = self.occupied_coordinates[0][0]
        if y == "": y = self.occupied_coordinates[0][1]

        occupied_coordinates = [(x,y),(x+1,y),(x+1,y-1),(x+2,y-1)]

        if self.check(occupied_coordinates):
            self.erase()
            super().__init__(self.color, occupied_coordinates)
            self.occupied_coordinates = occupied_coordinates

class Z(Shape):
    def __init__(self, x, y, color):
        occupied_coordinates = [(x,y),(x+1,y),(x+1,y+1),(x+2,y+1)]

        if self.check(occupied_coordinates):
            super().__init__(color, occupied_coordinates)
            self.occupied_coordinates = occupied_coordinates

    def move(self, x="", y=""):
        if x == "": x = self.occupied_coordinates[0][0]
        if y == "": y = self.occupied_coordinates[0][1]

        occupied_coordinates = [(x,y),(x+1,y),(x+1,y+1),(x+2,y+1)]

        if self.check(occupied_coordinates):
            self.erase()
            super().__init__(self.color, occupied_coordinates)
            self.occupied_coordinates = occupied_coordinates

class L(Shape):
    def __init__(self, x, y, color):
        occupied_coordinates = [(x,y),(x+1,y),(x,y-1),(x,y-2)]

        if self.check(occupied_coordinates):
            super().__init__(color, occupied_coordinates)
            self.occupied_coordinates = occupied_coordinates

    def move(self, x="", y=""):
        if x == "": x = self.occupied_coordinates[0][0]
        if y == "": y = self.occupied_coordinates[0][1]

        occupied_coordinates = [(x,y),(x+1,y),(x,y-1),(x,y-2)]

        if self.check(occupied_coordinates):
            self.erase()
            super().__init__(self.color, occupied_coordinates)
            self.occupied_coordinates = occupied_coordinates

class J(Shape):
    def __init__(self, x, y, color):
        occupied_coordinates = [(x,y),(x+1,y),(x+1,y-1),(x+1,y-2)]

        if self.check(occupied_coordinates):
            super().__init__(color, occupied_coordinates)
            self.occupied_coordinates = occupied_coordinates

    def move(self, x="", y=""):
        if x == "": x = self.occupied_coordinates[0][0]
        if y == "": y = self.occupied_coordinates[0][1]

        occupied_coordinates = [(x,y),(x+1,y),(x+1,y-1),(x+1,y-2)]

        if self.check(occupied_coordinates):
            self.erase()
            super().__init__(self.color, occupied_coordinates)
            self.occupied_coordinates = occupied_coordinates

class T(Shape):
    def __init__(self, x, y, color):
        occupied_coordinates = [(x,y),(x+1,y),(x+2,y),(x+1,y+1)]

        if self.check(occupied_coordinates):
            super().__init__(color, occupied_coordinates)
            self.occupied_coordinates = occupied_coordinates

    def move(self, x="", y=""):
        if x == "": x = self.occupied_coordinates[0][0]
        if y == "": y = self.occupied_coordinates[0][1]

        occupied_coordinates = [(x,y),(x+1,y),(x+2,y),(x+1,y+1)]

        if self.check(occupied_coordinates):
            self.erase()
            super().__init__(self.color, occupied_coordinates)
            self.occupied_coordinates = occupied_coordinates


def draw_window(w, h):
    black = (0, 0, 0)

    left_top = (100, 100)
    right_top = (100, h)
    left_bottom = (w, 100)
    right_bottom = (w, h)

    pygame.draw.line(screen, black, left_top, right_top, 2)
    pygame.draw.line(screen, black, right_top, right_bottom, 2)
    pygame.draw.line(screen, black, right_bottom, left_bottom, 2)
    pygame.draw.line(screen, black, left_bottom, left_top, 2)

    for x in range(100,300,20):
        if x!=100:
            pygame.draw.line(screen, black, (x,100), (x,h), 2)

    for y in range(100,500,20):
        if y != 100:
            pygame.draw.line(screen, black, (100, y), (w, y), 2)

    pygame.display.flip()

def color_box(coordinates,color):
    x = coordinates[0]
    y = coordinates[1]
    real_x = (100 + (x * 20)) + 2
    real_y = (100 + (y * 20)) + 2

    pygame.draw.rect(screen, color, pygame.Rect(real_x, real_y, 18, 18))

    pygame.display.flip()


SHAPES = [O,I,S,Z,L,J,T]
COLORS = [(0,255,255),(255, 255, 0),(128, 0, 128),(0, 255, 0),
          (255, 0, 0),(0, 0, 255),(255, 127, 0),(127, 127, 127)]
bottom_boxs = set()
for x in range(0, 10):bottom_boxs.add((x, 19))

background_colour = (255,255,255)

(width, height) = (400, 600)

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('Tutorial 1')

screen.fill(background_colour)

pygame.display.flip()

draw_window(width-100,height-100)

current_figure = ""
last_events = []

running = True

while running:
    if current_figure == "" or current_figure.is_at_bottom():
        current_figure = choice(SHAPES)(randint(5, 7), randint(5, 8), choice(COLORS))

    events = pygame.event.get()

    if events != []:
        for event in events:
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                    try:
                        if event.key == pygame.K_LEFT:
                            current_figure.move(current_figure.occupied_coordinates[0][0]-1)
                        if event.key == pygame.K_RIGHT:
                            current_figure.move(current_figure.occupied_coordinates[0][0]+1)
                        if event.key == pygame.K_DOWN:
                            current_figure.move(y=current_figure.occupied_coordinates[0][1] + 1)
                        if event.key == pygame.K_UP:pass

                    except ValueError:pass

                    if current_figure.is_at_bottom():
                        current_figure.add_at_bottom()


#
# events = pygame.event.get()
#
# if events != []:
#     for event in events:
#         if event.type == pygame.QUIT:
#           running = False
#
#         if event.type == pygame.KEYDOWN:
#             try:
#                 if not current_figure.is_at_bottom():
#
#                     if event.key == pygame.K_LEFT:
#                         current_figure.move(current_figure.occupied_coordinates[0][0]-1)
#                     if event.key == pygame.K_RIGHT:
#                         current_figure.move(current_figure.occupied_coordinates[0][0]+1)
#                     if event.key == pygame.K_DOWN:
#                         current_figure.move(y=current_figure.occupied_coordinates[0][1] + 1)
#                     if event.key == pygame.K_UP:
#                         pass
#
#                     if current_figure.is_at_bottom():
#                         try:
#                             current_figure.add_at_bottom()
#                         except AttributeError:
#                             pass
#                         continue
#
#
#
#             except AttributeError:
#                 pass
#     if last_events != []:
#         current_figure.move(y=current_figure.occupied_coordinates[0][1] + 1)
# else:
#     current_figure.move(y=current_figure.occupied_coordinates[0][1] + 1)
# time.sleep(1)
#
# last_events = events
#
# if current_figure.is_at_bottom():
#     try:
#         current_figure.add_at_bottom()
#     except AttributeError:pass

