import pygame
import time
from random import choice
from random import randint

########################################################################################################################
##################################################### Constants ########################################################
########################################################################################################################

COLORS = [(0,255,255),(255, 255, 0),(128, 0, 128),(0, 255, 0),
          (255, 0, 0),(0, 0, 255),(255, 127, 0),(127, 127, 127)]

BLACK = (0, 0, 0)

BACKGROUND_COLOR = (255,255,255)

SHAPES = ["0","I","S","Z","L","J","T"]

########################################################################################################################
##################################################### Classes  #########################################################
########################################################################################################################

class Shape:
    def __init__(self,name,x,y,color):

        future_coordinates = self.generate_coordinates(x,y,name)

        try:
            if not self.is_occupied(future_coordinates):
                self.is_disabled = False
                self.name = name
                self.rotation = 0
                self.cc = future_coordinates
                self.color = color

                self.draw()
        except TypeError:
            pass

    @staticmethod
    def generate_coordinates(x, y, name):
        if name == "O":
            return [(x,y),(x,y-1),(x+1,y-1),(x+1,y)]
        elif name == "I":
            return [(x,y),(x,y-1),(x,y-2),(x,y-3)]
        elif name == "S":
            return [(x,y),(x+1,y),(x+1,y-1),(x+2,y-1)]
        elif name == "Z":
            return [(x,y),(x+1,y),(x+1,y+1),(x+2,y+1)]
        elif name == "L":
            return [(x,y),(x-1,y),(x-1,y-1),(x-1,y-2)]
        elif name == "J":
            return [(x,y),(x+1,y),(x+1,y-1),(x+1,y-2)]
        elif name == "T":
            return [(x,y),(x+1,y),(x+2,y),(x+1,y+1)]

    @staticmethod
    def is_occupied(coordinates):
        for each in coordinates:
            if each in occupied_coordinates:
                return each
        return False

    def draw(self):
        for each in self.cc:color_box(screen,each, self.color)

    def erase(self):
        for each in self.cc: color_box(screen, each, BACKGROUND_COLOR)

    def rotate_coordinates(self):
        if self.name == "O":return self.cc

        elif self.name == "I":
            if self.rotation == 0:
                return [(self.cc[0][0]-1,self.cc[0][1]-2),(self.cc[1][0],self.cc[1][1]-1),
                        (self.cc[2][0]+1,self.cc[2][1]),(self.cc[3][0]+2,self.cc[3][1]+1)]

            elif self.rotation == 1:
                return [(self.cc[0][0]+2, self.cc[0][1]-1), (self.cc[1][0]+1, self.cc[1][1]),
                        (self.cc[2][0], self.cc[2][1]+1), (self.cc[3][0]-1, self.cc[3][1]+2)]

            elif self.rotation == 2:
                return [(self.cc[0][0]+1, self.cc[0][1]+2),(self.cc[1][0], self.cc[1][1]+1),
                        (self.cc[2][0]-1, self.cc[2][1]),(self.cc[3][0]-2, self.cc[3][1]-1)]

            elif self.rotation == 3:
                return [(self.cc[0][0] - 2, self.cc[0][1] + 1), (self.cc[1][0] - 1, self.cc[1][1]),
                        (self.cc[2][0], self.cc[2][1] - 1), (self.cc[3][0] + 1, self.cc[3][1] - 2)]

            elif self.rotation == 4:
                self.rotation = 0
                return self.rotate_coordinates()

        elif self.name == "S":
            if self.rotation == 0:
                return [(self.cc[0][0] + 1, self.cc[0][1] - 1), (self.cc[1][0], self.cc[1][1]),
                        (self.cc[2][0]+1, self.cc[2][1] + 1), (self.cc[3][0], self.cc[3][1] + 2)]
            elif self.rotation == 1:
                return [(self.cc[0][0] + 1, self.cc[0][1] + 1), (self.cc[1][0], self.cc[1][1]),
                        (self.cc[2][0] - 1, self.cc[2][1] + 1), (self.cc[3][0]-2, self.cc[3][1])]
            elif self.rotation == 2:
                return [(self.cc[0][0] - 1, self.cc[0][1] + 1), (self.cc[1][0], self.cc[1][1]),
                        (self.cc[2][0] - 1, self.cc[2][1]-1), (self.cc[3][0], self.cc[3][1]-2)]
            elif self.rotation == 3:
                return [(self.cc[0][0] - 1, self.cc[0][1] - 1), (self.cc[1][0], self.cc[1][1]),
                        (self.cc[2][0] + 1, self.cc[2][1] - 1), (self.cc[3][0]+2, self.cc[3][1])]
            elif self.rotation == 4:
                self.rotation = 0
                return self.rotate_coordinates()

        elif self.name == "Z":
            if self.rotation == 0:
                return [(self.cc[0][0]+2, self.cc[0][1]), (self.cc[1][0]+1, self.cc[1][1]+1),
                        (self.cc[2][0], self.cc[2][1]), (self.cc[3][0]-1, self.cc[3][1]+1)]
            elif self.rotation == 1:
                return [(self.cc[0][0], self.cc[0][1]+2), (self.cc[1][0]-1, self.cc[1][1]+1),
                        (self.cc[2][0], self.cc[2][1]), (self.cc[3][0]-1, self.cc[3][1]-1)]
            elif self.rotation == 2:
                return [(self.cc[0][0]-2, self.cc[0][1]), (self.cc[1][0]-1, self.cc[1][1]-1),
                        (self.cc[2][0], self.cc[2][1]), (self.cc[3][0]+1, self.cc[3][1]-1)]
            elif self.rotation == 3:
                return [(self.cc[0][0], self.cc[0][1]-2), (self.cc[1][0]+1, self.cc[1][1]-1),
                        (self.cc[2][0], self.cc[2][1]), (self.cc[3][0]+1, self.cc[3][1]+1)]
            elif self.rotation == 4:
                self.rotation = 0
                return self.rotate_coordinates()

        elif self.name == "L":
            if self.rotation == 0:
                return [(self.cc[0][0]-2, self.cc[0][1]), (self.cc[1][0]-1, self.cc[1][1]-1),
                        (self.cc[2][0], self.cc[2][1]), (self.cc[3][0]+1, self.cc[3][1]+1)]
            elif self.rotation == 1:
                return [(self.cc[0][0], self.cc[0][1]-2), (self.cc[1][0]+1, self.cc[1][1]-1),
                        (self.cc[2][0], self.cc[2][1]), (self.cc[3][0]-1, self.cc[3][1]+1)]
            elif self.rotation == 2:
                return [(self.cc[0][0]+2, self.cc[0][1]), (self.cc[1][0]+1, self.cc[1][1]+1),
                        (self.cc[2][0], self.cc[2][1]), (self.cc[3][0]-1, self.cc[3][1]-1)]
            elif self.rotation == 3:
                return [(self.cc[0][0], self.cc[0][1]+2), (self.cc[1][0]-1, self.cc[1][1]+1),
                        (self.cc[2][0], self.cc[2][1]), (self.cc[3][0]+1, self.cc[3][1]-1)]
            elif self.rotation == 4:
                self.rotation = 0
                return self.rotate_coordinates()

        elif self.name == "J":
            if self.rotation == 0:
                return [(self.cc[0][0], self.cc[0][1]-2), (self.cc[1][0] - 1, self.cc[1][1] - 1),
                        (self.cc[2][0], self.cc[2][1]), (self.cc[3][0] + 1, self.cc[3][1] + 1)]
            elif self.rotation == 1:
                return [(self.cc[0][0] +2, self.cc[0][1]), (self.cc[1][0] + 1, self.cc[1][1] - 1),
                        (self.cc[2][0], self.cc[2][1]), (self.cc[3][0] - 1, self.cc[3][1] + 1)]
            elif self.rotation == 2:
                return [(self.cc[0][0], self.cc[0][1]+2), (self.cc[1][0] + 1, self.cc[1][1] + 1),
                        (self.cc[2][0], self.cc[2][1]), (self.cc[3][0] - 1, self.cc[3][1] - 1)]
            elif self.rotation == 3:
                return [(self.cc[0][0]-2, self.cc[0][1]), (self.cc[1][0] - 1, self.cc[1][1] + 1),
                        (self.cc[2][0], self.cc[2][1]), (self.cc[3][0] + 1, self.cc[3][1] - 1)]
            elif self.rotation == 4:
                self.rotation = 0
                return self.rotate_coordinates()

        elif self.name == "T":
            if self.rotation == 0:
                return [(self.cc[0][0]+1, self.cc[0][1]-1), (self.cc[1][0], self.cc[1][1]),
                        (self.cc[2][0]-1, self.cc[2][1]+1), (self.cc[3][0]-1, self.cc[3][1]-1)]
            elif self.rotation == 1:
                return [(self.cc[0][0]+1, self.cc[0][1]+1), (self.cc[1][0], self.cc[1][1]),
                        (self.cc[2][0]-1, self.cc[2][1]-1), (self.cc[3][0]+1, self.cc[3][1]-1)]
            elif self.rotation == 2:
                return [(self.cc[0][0]-1, self.cc[0][1]+1), (self.cc[1][0], self.cc[1][1]),
                        (self.cc[2][0]+1, self.cc[2][1]-1), (self.cc[3][0]+1, self.cc[3][1]+1)]
            elif self.rotation == 3:
                return [(self.cc[0][0]-1, self.cc[0][1]-1), (self.cc[1][0], self.cc[1][1]),
                        (self.cc[2][0]+1, self.cc[2][1]+1), (self.cc[3][0]-1, self.cc[3][1]+1)]
            elif self.rotation == 4:
                self.rotation = 0
                return self.rotate_coordinates()



    def move(self,direction):
        try:
            if direction == "right":
                future_coordinates = [(self.cc[0][0]+1,self.cc[0][1]),(self.cc[1][0]+1,self.cc[1][1]),
                                      (self.cc[2][0]+1,self.cc[2][1]),(self.cc[3][0]+1,self.cc[3][1])]
            elif direction == "left":
                future_coordinates = [(self.cc[0][0] - 1, self.cc[0][1]), (self.cc[1][0] - 1, self.cc[1][1]),
                                      (self.cc[2][0] - 1, self.cc[2][1]), (self.cc[3][0] - 1, self.cc[3][1])]
            elif direction == "down":
                future_coordinates = [(self.cc[0][0], self.cc[0][1]+1), (self.cc[1][0], self.cc[1][1]+1),
                                      (self.cc[2][0], self.cc[2][1]+1), (self.cc[3][0], self.cc[3][1]+1)]
            elif direction == "rotate":
                future_coordinates = self.rotate_coordinates()
        except:
            self.move(direction)

        try:
            if not self.is_occupied(future_coordinates):
                if direction == "rotate":
                    self.rotation += 1
                self.erase()
                self.cc = future_coordinates
                self.draw()
            else:
                if direction == "down":
                    conflict = self.is_occupied(future_coordinates)
                    if not conflict in non_disable_conflict_coordinates:
                        self.is_disabled = True
                        for each in self.cc:
                            occupied_coordinates.add(each)
                            coordinates_into_color[each] = self.color



        except TypeError:pass

########################################################################################################################
##################################################### Functions ########################################################
########################################################################################################################

def createDisplay(size,name):
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption(name)

    screen.fill(BACKGROUND_COLOR)

    pygame.display.flip()

    return screen

def drawWindow(w, h):
    screen = createDisplay((w+100,h+100),"Tetris")

    # Draw horizontal lines
    for x in range(100,320,20):pygame.draw.line(screen, BLACK, (x,100), (x,h), 2)

    # Draw vertical lines
    for y in range(100,520,20):pygame.draw.line(screen, BLACK, (100, y), (w, y), 2)

    pygame.display.flip()

    return screen

def color_box(screen, coordinates,color):
    x = coordinates[0]
    y = coordinates[1]

    real_x = (100 + (x * 20)) + 2
    real_y = (100 + (y * 20)) + 2

    pygame.draw.rect(screen, color, pygame.Rect(real_x, real_y, 18, 18))

    pygame.display.flip()

def clear_line(line):
    for each in line:
        color_box(screen,each,BACKGROUND_COLOR)
        for each in line:
            if each in occupied_coordinates:
                occupied_coordinates.remove(each)

    line_row = line[0][1]-1
    for y in range(line_row, -1, -1):
        for x in range(0, 10):
            try:
                color = coordinates_into_color[(x,y)]
            except:
                color = BACKGROUND_COLOR

            color_box(screen,(x,y+1),color)

            coordinates_into_color[(x, y+1)] = color

            if color == BACKGROUND_COLOR and (x,y+1) in occupied_coordinates:
                occupied_coordinates.remove((x,y+1))
            elif color != BACKGROUND_COLOR:
                occupied_coordinates.add((x,y+1))
                occupied_coordinates.remove((x,y))

def check_for_full_lines():
    line = []
    for y in range(0,20):
        count = 0
        for x in range(0,10):
            line.append((x,y))

        for each in line:
            if each in occupied_coordinates:
                count += 1

        if count == 10:
            clear_line(line)
        line.clear()



########################################################################################################################
####################################################### Flow ###########################################################
########################################################################################################################

occupied_coordinates = set()

for x in range(-1,11):
    for y in range(-1,21):
        if x == -1 or x == 10:occupied_coordinates.add((x,y))
        elif y == -1 or y == 20:occupied_coordinates.add((x,y))

non_disable_conflict_coordinates = set()

for x in range(-1,11):
    for y in range(-1,20):
        if x == -1 or x == 10:non_disable_conflict_coordinates.add((x,y))
        elif y == -1 or y == 20:non_disable_conflict_coordinates.add((x,y))

coordinates_into_color = {}

screen = drawWindow(300,500)

figure = ""
last_event = ""

running = True

while running:
    try:
        if figure == "" or figure.is_disabled:
            figure = Shape(choice(SHAPES), 5, 5, choice(COLORS))
    except AttributeError:
        figure = Shape(choice(SHAPES), 5, 5, choice(COLORS))

    events = pygame.event.get()
    if events != []:
        for event in events:
            if event.type == pygame.QUIT:
              running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:figure.move("left")
                if event.key == pygame.K_RIGHT:figure.move("right")
                if event.key == pygame.K_DOWN:figure.move("down")
                if event.key == pygame.K_UP:figure.move("rotate")
                time.sleep(0.2)

    figure.move("down")
    time.sleep(0.5)

    last_event = events

    check_for_full_lines()