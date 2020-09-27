from display.Cube2DDisplay import Cube2DDisplay
from display.Sequence2DDisplay import Sequence2DDisplay
from models.Cube import Cube


if __name__ == '__main__':
    cube = Cube()

    seq = ('R', 'U', 'R\'', 'U\'')
    # for _ in range(6):
    #     for letter in seq:
    #         cube.moves.moveFromLetter(letter)
    
    """
        Indices sont inverses pour la face 5
        swapTop ne prend pas la bonne chose que ce soit avec
        le decorateur ou non
    """

    if 0:
        
        cubeDisplay = Sequence2DDisplay(cube)
        cubeDisplay.display(seq)
    else:
        # cube.moves.up()
        for i in range(5):
            cube.faces[i].stickers[0] = 'Z'
        cube.faces[5].stickers[-1] = 'Z'

        for i in range(5):
            cube.faces[i].stickers[3] = 'U'
        cube.faces[5].stickers[-4] = 'U'

        cube.moves.moveFromLetter('Y')

        cubeDisplay = Cube2DDisplay(cube)
        cubeDisplay.display()

"""
    :TODO:
        - Rotate faces
"""