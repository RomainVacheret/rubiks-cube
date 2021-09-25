from __future__ import annotations
from typing import Final, Generator, NoReturn

from rubiks_cube.moves import Moves
from rubiks_cube.exceptions import InvalidLineIndexException, InvalidLayerIndexException
# https://en.wikipedia.org/wiki/Rubik%27s_Cube

# TODO: replace with an enum
COLORS: Final = ('WHITE', 'RED', 'BLUE', 'ORANGE', 'GREEN', 'YELLOW')


class Face:
    """ Represents a Rubik's cube face which is 
        composed of 9 stickers. 
        To complete a face each sticker must have the same 
        color.
        
    """
    def __init__(self, color: str):
        """
            Initializes the face according to the color passed by argument.
            :param color: Color of the face 
        """
        self.stickers = [color[0] for _ in range(9)]

    @property
    def color(self) -> str:
        """ Represents the starting color of the face. """
        # the 4th index is the center (which never changes)
        return self.stickers[4]

    @property
    def is_completed(self) -> bool:
        """ Informs if the face is completed. """
        return all(sticker == self.color for sticker in self.stickers)

    def line_is_completed(self, index: int) -> bool:
        """ Check if all three sticker of a sticker line are of the 
            same color. 
            Note that the color must be the face's color. 
            
            :param index: Index of the checked line.

            :raises InvalidLineIndexException: index must be between 0 included and 3 excluded.
            
            :returns: The color of each sticker is the same or not.
        """
        if  index > 2 or index < 0:
            raise InvalidLineIndexException('Line index must be betwen 0 and 2 (both included)')

        starting_index = index * 3
        color = self.stickers[starting_index]
        return self.stickers[starting_index:starting_index + 3] \
            .count(color) == 3 and color == self.color

    def line_generator(self) -> Generator[list[str]]:
        """ Yields each line of the current face. """
        for index in range(0, 9, 3):
            yield self.stickers[index:index + 3]    

    @staticmethod
    def rotate_stickers(stickers: list[str]) -> list[str]:
        new = []
        idx = 6
        for _ in range(3):
            for i in range(3):
                new.append(stickers[idx - (3 * i)])
            idx += 1
        
        return new
    
    def rotate_clockwise(self) -> NoReturn:
        self.stickers = self.rotate_stickers(self.stickers)
    
    def rotate_anti_clockwise(self) -> NoReturn:
        self.stickers = self.rotate_stickers(self.stickers)[::-1]
    
    def __eq__(self, obj: object) -> bool:
        return all(self.stickers[idx] == obj.stickers[idx] for idx in range(9))

    def __repr__(self) -> str:
        return f'[{" ".join(self.stickers)}]'
        

class Cube:
    """ Represents a Rubik's cube which is 
        composed of 6 faces.
        Each face has a different color (from the list above). 
        The symetric list index are opposite (Exp : first and last).
        To finish the puzzle, each face must be completed.
        
    """
    def __init__(self):
        self.faces = [Face(color) for color in COLORS]
        self.moves = Moves(self)

    @property
    def is_completed(self) -> bool:
        """ Informs if the color of each sticker is the same or not. """
        return all(face.is_completed for face in self.faces)

    def layer_is_completed(self, index: int) -> NoReturn:
        """ Checks if a given layer is completed or not.
            
            :param index: Index of the checked layer.

            :raises InvalidLayerIndexException:

            :returns: The color is the same for each sticker from a given layer.
        """
        if  index > 2 or index < 0:
            raise InvalidLayerIndexException('Layer index must be betwen 0 and 2 (both included)')

        check = lambda face, index: face.line_is_completed(index) \
            and face.stickers[index * 2] == face.color
        return all(check(face, index) for face in self.faces)
    
    def display(self) -> NoReturn:
        """ Displays the Rubik's cube pattern as the following:
            - Orange 
            - Green, White, Blue
            - Red
            - Yellow

            TODO -> BROKEN
        """
        results = [self.faces[index].line_generator() for index in range(6)]

        # TODO: improve name
        def display_line(*args: tuple[int]) -> str:
            """ Displays a line for one or three faces. 

                :param args: Index of the face(s) to print.

                :returns: The line to print.
            """
            display_face_line = lambda id: ' '.join(results[id].__next__())
            string = '  '.join(display_face_line(arg) for arg in args)
            if len(args) == 1:
                string = '{}{}'.format(' ' * 7, string)
            return string

        def three_times(func: callable) -> NoReturn:
            """ Executes the function 3 times before \n. """
            for _ in range(3):
                print(func)
            print()

        three_times(display_line(3))
        three_times(display_line(4, 0, 2))
        three_times(display_line(1))
        three_times(display_line(5))

    
    def __eq__(self, obj: object) -> bool:
        return all(self.faces[idx] == obj.faces[idx] for idx in range(6))
    
    def __repr__(self) -> str:
        return f'[{" ".join(map(str, self.faces))}]'