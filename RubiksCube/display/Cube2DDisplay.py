import pygame
import sys

from models.Cube import Cube

# Sticker colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 140, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
# Backgroup
GREY = (169, 169, 169)

STICKER_TO_COLOR = {
    'W': WHITE,
    'R': RED,
    'B': BLUE,
    'O': ORANGE,
    'G': GREEN,
    'Y': YELLOW,
    'Z': (0, 0, 0),
    'X': GREY
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
    
    def mainLoop(self):
        """ Maintains the window displayed. """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
    
    def displayFace(self, face, xPos, yPos):
        """ Displays a face.

            :param face: Face which is displayed.
            :type face: Face
            :param xPos: Stating x coordonates.
            :type xPos: int 
            :param yPos: Starting y coordonates.
            :type yPos: int
        """
        xPos_ = xPos
        yPos_ = yPos
        for line in face.lineGenerator():
            for sticker in line:
                pygame.draw.rect(
                    self.surface,
                    STICKER_TO_COLOR[sticker],
                    (
                        xPos_, 
                        yPos_, 
                        STICKER_LENGTH - 2, 
                        STICKER_LENGTH - 2
                    )
                )
                xPos_ += STICKER_LENGTH
            xPos_ = xPos
            yPos_ += STICKER_LENGTH
        
    def updateDisplay(self):
        # ORANGE
        # self.cube.faces[3].frontMove()
        # self.cube.faces[3].frontMove()
        self.displayFace(self.cube.faces[3], LINE_LENGTH , 0)
        # # GREEN WHITE BLUE
        # self.cube.faces[4].frontMove(False)
        # self.cube.faces[4].frontMove(False)
        self.displayFace(self.cube.faces[4], 0, LINE_LENGTH)
        self.displayFace(self.cube.faces[0], LINE_LENGTH, LINE_LENGTH)
        # self.cube.faces[2].frontMove()
        # self.cube.faces[2].frontMove()
        self.displayFace(self.cube.faces[2], LINE_LENGTH * 2, LINE_LENGTH)
        # RED 
        self.displayFace(self.cube.faces[1], LINE_LENGTH, 2 * LINE_LENGTH)
        # YELLOW
        # self.cube.faces[5].frontMove()
        # self.cube.faces[5].frontMove()
        self.displayFace(self.cube.faces[5], LINE_LENGTH, 3 * LINE_LENGTH)
        
        
    def display(self):
        """ Displays the cube pattern. 

            :TODO: Use deep copy to save sove rotations ?
        """
        self.updateDisplay()
        self.mainLoop()

        # Get back to normal 
        # self.cube.faces[3].frontMove()
        # self.cube.faces[3].frontMove()
        # self.cube.faces[4].frontMove(False)
        # self.cube.faces[4].frontMove(False)
        # self.cube.faces[2].frontMove()
        # self.cube.faces[2].frontMove()
        # self.cube.faces[5].frontMove()
        # self.cube.faces[5].frontMove()

