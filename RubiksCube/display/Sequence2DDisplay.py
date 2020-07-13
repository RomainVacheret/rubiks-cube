import pygame 
import sys

from display.Cube2DDisplay import Cube2DDisplay

class Sequence2DDisplay(Cube2DDisplay):
    def mainLoop(self, sequence):
        """ Maintains the window displayed. 
            While it is displayed press 'q' (for azerty) keyboard
            to display the next state until the sequence of moves is completed.

            :param sequence:
            :param sequence: Move sequence.
            :type sequence: list[str]
        """
        # Returns a generator
        sequenceGen = self.displaySequence(sequence) 
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        # While there are some changes to be made
                        try:
                            sequenceGen.__next__()
                        except StopIteration:
                            pass

            pygame.display.update()
    
    def displaySequence(self, sequence):
        """ Returns a generator of changed displays made according 
            to the given sequence of moves.

            :param sequence: Move sequence.
            :type sequence: list[str]

            :rtype: Generator
        """
        for letter in sequence:
            self.cube.moves.moveFromLetter(letter)
            super().updateDisplay()
            yield

    def display(self, sequence):
        """ Displays the cube pattern. """
        super().updateDisplay()
        self.mainLoop(sequence)