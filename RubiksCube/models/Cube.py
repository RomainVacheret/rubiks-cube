from .Face import Face
from .Moves import Moves
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
    def isCompleted(self):
        """ Informs the color of each sticker is the same. """
        return all(face for face in self.faces)

    def layerIsCompleted(self, index):
        """ Check if a given layer is completed or not.
            
            :param index: Layer index between 0 included and 3 excluded.
            :type index: int

            :return: The color is the same for each sticker from a given layer.
            :rtype: bool
        """
        assert 0 <= index < 3
        check = lambda face, index: face.lineIsCompleted(index) \
            and face.stickers[index * 2] == face.color
        return all(check(face, index) for face in self.faces)
    
    def display(self):
        """ Displays the Rubik's cube pattern as the following:
            - Orange 
            - Green, White, Blue
            - Red
            - Yellow
        """
        results = [self.faces[index].lineGenerator() for index in range(6)]

        def displayLine(*args):
            """ Displays a line for one or three faces. 

                :param args: Index of the face(s) to print.
                :type args: int or tuple(int)

                :return: The line to print.
                :rtype: str
            """
            displayFaceLine = lambda id: ' '.join(results[id].__next__())
            string = '  '.join(displayFaceLine(arg) for arg in args)
            if len(args) == 1:
                string = '{}{}'.format(' ' * 7, string)
            return string

        def threeTimes(func):
            """ Executes the function 3 times before \n. """
            for _ in range(3):
                print(func)
            print()

        threeTimes(displayLine(3))
        threeTimes(displayLine(4, 0, 2))
        threeTimes(displayLine(1))
        threeTimes(displayLine(5))

    
    def faceRotation(self, index):
        pass
    

if __name__ == '__main__':
    cube = Cube()
    # cube.faces[3].stickers[1] = 'BLACK'
    # for i in range(3):
    #     print(cube.layerIsCompleted(i))
    cube.display()


"""
    :TODO:
        - Create moves for one face only + move faces 
"""