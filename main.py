from rubiks_cube.display.cube_2d_display import Cube2DDisplay
from rubiks_cube.display.sequence_2d_display import Sequence2DDisplay
from rubiks_cube.cube import Cube
from rubiks_cube.moves import Moves

import random


if __name__ == '__main__':
    cube = Cube()

    move_sequence = [random.choice(Moves.LETTERS) for _ in range(20)]
    cube_display = Sequence2DDisplay(cube)
    cube_display.display(move_sequence)