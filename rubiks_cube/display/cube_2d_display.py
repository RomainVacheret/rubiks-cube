import pygame
import sys

from rubiks_cube.cube import Cube

# Sticker colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 140, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
# Background
GREY = (169, 169, 169)

STICKER_TO_COLOR = {
    'W': WHITE,
    'R': RED,
    'B': BLUE,
    'O': ORANGE,
    'G': GREEN,
    'Y': YELLOW,
    'Z': (0, 0, 0),
    'X': GREY,
    'U': (50, 50, 50),
}

STICKER_LENGTH = 30
LINE_LENGTH = 3 * STICKER_LENGTH


class Cube2DDisplay:
    def __init__(self, cube):
        pygame.init()
        pygame.display.set_caption('Rubik\'s cube')
        self.surface = pygame.display.set_mode((3 * LINE_LENGTH, 4 * LINE_LENGTH))
        self.surface.fill(GREY)
        self.cube = cube
    
    def main_loop(self):
        """ Maintains the window displayed. """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
    
    def display_face(self, face, x_pos, y_pos):
        """ Displays a face.

            :param face: Face which is displayed.
            :type face: Face
            :param x_pos: Stating x coordonate.
            :type x_pos: int 
            :param y_pos: Starting y coordonate.
            :type y_pos: int
        """
        x_pos_ = x_pos
        y_pos_ = y_pos

        for line in face.line_generator():
            for sticker in line:
                pygame.draw.rect(
                    self.surface,
                    STICKER_TO_COLOR[sticker],
                    (
                        x_pos_, 
                        y_pos_, 
                        STICKER_LENGTH - 2, 
                        STICKER_LENGTH - 2
                    )
                )
                x_pos_ += STICKER_LENGTH

            x_pos_ = x_pos
            y_pos_ += STICKER_LENGTH
        
    def update_display(self):
        """ Redraws the screen. """
        # ORANGE
        self.display_face(self.cube.faces[3], LINE_LENGTH , 0)
        # GREEN WHITE BLUE
        self.display_face(self.cube.faces[4], 0, LINE_LENGTH)
        self.display_face(self.cube.faces[0], LINE_LENGTH, LINE_LENGTH)
        self.display_face(self.cube.faces[2], LINE_LENGTH * 2, LINE_LENGTH)
        # RED 
        self.display_face(self.cube.faces[1], LINE_LENGTH, 2 * LINE_LENGTH)
        # YELLOW
        self.display_face(self.cube.faces[5], LINE_LENGTH, 3 * LINE_LENGTH)
        
    def display(self):
        """ Displays the cube pattern

            :TODO: Use deep copy to save rotations ?
        """
        self.update_display()
        self.main_loop()


