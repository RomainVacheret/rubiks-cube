from rubiks_cube.moves import Moves
# https://en.wikipedia.org/wiki/Rubik%27s_Cube

COLORS = ('WHITE', 'RED', 'BLUE', 'ORANGE', 'GREEN', 'YELLOW')

CONFIGURATIONS = {
    'WHITE': ('ORANGE', 'BLUE', 'RED', 'GREEN'),
    'RED': ('YELLOW', 'GREEN', 'WHITE', 'BLUE'),
    'BLUE': ('RED', 'WHITE', 'ORANGE', 'YELLOW'),
    'ORANGE': ('WHITE', 'GREEN', 'YELLOW', 'BLUE'),
    'GREEN': ('RED', 'YELLOW', 'ORANGE', 'WHITE'),
    'YELLOW': ('ORANGE', 'GREEN', 'RED', 'BLUE'),
}


class Face:
    """ Represents a Rubik's cube face which is 
        composed of 9 stickers. 
        To complete a face each sticker must have the same 
        color.
        
    """
    def __init__(self, color):
        self.stickers = [color[0] for _ in range(9)]

    @property
    def color(self):
        """ Reprensents the starting color of the face. """
        # the 4th index is the center (which never changes)
        return self.stickers[4]

    @property
    def is_completed(self):
        """ Informs if each face is completed. """
        return all(sticker == self.color for sticker in self.stickers)

    def line_is_completed(self, index):
        """ Check if all three sticker of sticker line are of the 
            same color. 
            Note that the color must be the face's color. 
            
            :param index: Line index between 0 included and 3 excluded.
            :type index: int
            
            :return: The color of each sticker is the same or not.
            :rtype: bool
        """
        assert 0 <= index < 3
        starting_index = index * 3
        color = self.stickers[starting_index]
        return self.stickers[starting_index:starting_index + 3] \
            .count(color) == 3 and color == self.color

    def line_generator(self):
        """ Yields each line of the current face. """
        for index in range(0, 9, 3):
            yield self.stickers[index:index+3]
    
    def front_move(self, clockwise=True):
        """ Rotates the current face.
            
            :param clockwise: Clockwise or anticlockwise rotation.
            :type clockwise: bool
        """
        new = []
        idx = 6
        for _ in range(3):
            for i in range(3):
                new.append(self.stickers[idx - (3 * i)])
            idx += 1

        self.stickers = new if clockwise else new[::-1]


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
    def is_completed(self):
        """ Informs the color of each sticker is the same. """
        return all(face for face in self.faces)

    def layer_is_completed(self, index):
        """ Check if a given layer is completed or not.
            
            :param index: Layer index between 0 included and 3 excluded.
            :type index: int

            :return: The color is the same for each sticker from a given layer.
            :rtype: bool
        """
        assert 0 <= index < 3
        check = lambda face, index: face.line_is_completed(index) \
            and face.stickers[index * 2] == face.color
        return all(check(face, index) for face in self.faces)
    
    def display(self):
        """ Displays the Rubik's cube pattern as the following:
            - Orange 
            - Green, White, Blue
            - Red
            - Yellow
        """
        results = [self.faces[index].line_generator() for index in range(6)]

        def display_line(*args):
            """ Displays a line for one or three faces. 

                :param args: Index of the face(s) to print.
                :type args: int or tuple(int)

                :return: The line to print.
                :rtype: str
            """
            display_face_line = lambda id: ' '.join(results[id].__next__())
            string = '  '.join(display_face_line(arg) for arg in args)
            if len(args) == 1:
                string = '{}{}'.format(' ' * 7, string)
            return string

        def three_times(func):
            """ Executes the function 3 times before \n. """
            for _ in range(3):
                print(func)
            print()

        three_times(display_line(3))
        three_times(display_line(4, 0, 2))
        three_times(display_line(1))
        three_times(display_line(5))