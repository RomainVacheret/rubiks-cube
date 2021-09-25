from __future__ import annotations

import pygame 
import sys

from typing import NoReturn

from rubiks_cube.display.cube_2d_display import Cube2DDisplay

class Sequence2DDisplay(Cube2DDisplay):
    def main_loop(self, sequence: list[str]) -> NoReturn:
        """ Maintains the window displayed. 
            While it is displayed press 'q' (for azerty) keyboard
            to display the next state until the sequence of moves is completed.

            :param sequence:
            :param sequence: Move sequence.
            :type sequence: list[str]
        """
        # Returns a generator
        sequence_gen = self.display_sequence(sequence) 
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                    # if event.key == pygame.K_a:
                    # While there are some changes to be made
                    try:
                        sequence_gen.__next__()
                    except StopIteration:
                        pass

            pygame.display.update()
    
    def display_sequence(self, sequence: list[str]) -> NoReturn:
        """ Returns a generator of changed displays made according 
            to the given sequence of moves.

            :param sequence: Move sequence.
            :type sequence: list[str]

            :rtype: Generator
        """
        for letter in sequence:
            self.cube.moves.move_from_letter(letter)
            super().update_display()
            yield

    def display(self, sequence: list[str]) -> NoReturn:
        """ Displays the cube pattern. """
        super().update_display()
        self.main_loop(sequence)