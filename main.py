from rubiks_cube.display.cube_2d_display import Cube2DDisplay
from rubiks_cube.display.sequence_2d_display import Sequence2DDisplay
from rubiks_cube.cube import Cube


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

    if 1:
        
        cube_display = Sequence2DDisplay(cube)
        cube_display.display(seq)
    else:
        # cube.moves.up()
        for i in range(5):
            cube.faces[i].stickers[0] = 'Z'
        cube.faces[5].stickers[-1] = 'Z'

        for i in range(5):
            cube.faces[i].stickers[3] = 'U'
        cube.faces[5].stickers[-4] = 'U'

        cube.moves.move_from_letter('Y')

        cube_display = Cube2DDisplay(cube)
        cube_display.display()

"""
    :TODO:
        - Rotate faces
"""