from display.Cube2DDisplay import Cube2DDisplay
from display.Sequence2DDisplay import Sequence2DDisplay
from models.Cube import Cube


if __name__ == '__main__':
    cube = Cube()


    # cube.moves.down(False)


    # cube.faces[4].stickers[2] = 'Z'
    # cube.faces[2].stickers[2] = 'Z'
    # cube.moves.right()
    # cube.moves.turnDown()
    # cube.moves.right()


    # cube.moves.right()
    # cube.moves.turnLeft()
    # cube.faces[4].stickers[2] = 'Z'
    # cube.faces[2].stickers[2] = 'Z'
    # cube.faces[3].stickers[2] = 'Z'
    # cube.faces[1].stickers[2] = 'Z'
    # cube.moves.moveFromLetter('R')
    seq = ('R', 'U', 'R\'', 'U\'')
    for _ in range(6):
        for letter in seq:
            cube.moves.moveFromLetter(letter)

    
    
    # cube.faces[5].stickers = cube.faces[5].stickers[::-1]


    # cube.faces[5].stickers[0] = 'Z'
    
    """
        Indices sont inverses pour la face 5
        swapTop ne prend pas la bonne chose que ce soit avec
        le decorateur ou non
    """

    if 1:
        
        cubeDisplay = Sequence2DDisplay(cube)
        cubeDisplay.display(seq)
    else:
        # cube.moves.up()
        for i in range(5):
            cube.faces[i].stickers[0] = 'Z'
        cube.faces[5].stickers[-1] = 'Z'

        cubeDisplay = Cube2DDisplay(cube)
        cubeDisplay.display()

"""
    :TODO:
        - Rotate faces
"""