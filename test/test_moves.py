import unittest

from rubiks_cube.cube import Cube
from rubiks_cube.moves import Moves

class TestMoves(unittest.TestCase):
    
    def setUp(self):
        self.cube = Cube()
        self.moves = Moves(self.cube)

    def test__face_inverter(self):
        new_cube = Cube()
        new_cube.faces[0].stickers = ['W', 'R', 'B', 'O', 'G', 'Y', 'G', 'O', 'B']
        new_moves = Moves(new_cube)
        new_moves._face_inverter(0)
        self.assertTrue(new_cube.faces[0].stickers == ['B', 'O', 'G', 'Y', 'G', 'O', 'B', 'R', 'W'])

    def test_decorator(self):
        """ TODO """
        pass

    def test__swap_top(self):
        faces = [4, 0, 2, 5]
        new_cube = Cube()
        new_cube.moves._swap_top(*faces)

        test_cube = Cube()
        test_cube.faces[4].stickers[:3] = ['W'] * 3
        test_cube.faces[0].stickers[:3] = ['B'] * 3
        test_cube.faces[2].stickers[:3] = ['Y'] * 3
        test_cube.faces[5].stickers[:3] = ['G'] * 3
        self.assertTrue(test_cube == new_cube)

        faces = [4, 5, 2, 0]
        new_cube.moves._swap_top(*faces)
        self.assertTrue(new_cube == self.cube)

    def test__swap_bot(self):
        faces = [4, 0, 2, 5]
        new_cube = Cube()
        new_cube.moves._swap_bot(*faces)

        test_cube = Cube()
        test_cube.faces[4].stickers[-3:] = ['W'] * 3
        test_cube.faces[0].stickers[-3:] = ['B'] * 3
        test_cube.faces[2].stickers[-3:] = ['Y'] * 3
        test_cube.faces[5].stickers[-3:] = ['G'] * 3
        self.assertTrue(test_cube == new_cube)

        faces = [4, 5, 2, 0]
        new_cube.moves._swap_bot(*faces)
        self.assertTrue(new_cube == self.cube)

    def test__swap_left(self):
        faces = [0, 3, 5, 1]
        new_cube = Cube()
        new_cube.moves._swap_left(*faces)

        test_cube = Cube()
        test_cube.faces[0].stickers[0:7:3] = ['O'] * 3
        test_cube.faces[3].stickers[0:7:3] = ['Y'] * 3
        test_cube.faces[5].stickers[0:7:3] = ['R'] * 3
        test_cube.faces[1].stickers[0:7:3] = ['W'] * 3
        self.assertTrue(test_cube == new_cube)

        faces = [0, 1, 5, 3]
        new_cube.moves._swap_left(*faces)
        self.assertTrue(new_cube == self.cube)

    def test__swap_right(self):
        faces = [0, 3, 5, 1]
        new_cube = Cube()
        new_cube.moves._swap_right(*faces)

        test_cube = Cube()
        test_cube.faces[0].stickers[2:9:3] = ['O'] * 3
        test_cube.faces[3].stickers[2:9:3] = ['Y'] * 3
        test_cube.faces[5].stickers[2:9:3] = ['R'] * 3
        test_cube.faces[1].stickers[2:9:3] = ['W'] * 3
        self.assertTrue(test_cube == new_cube)

        faces = [0, 1, 5, 3]
        new_cube.moves._swap_right(*faces)
        self.assertTrue(new_cube == self.cube)

    def test_tmp(self):
        """ TODO """
        pass

    def test_front(self):
        new_cube = Cube()
        new_cube.moves.front()

        test_cube = Cube()
        test_cube.faces[1].stickers[:3] = ['B'] * 3
        test_cube.faces[2].stickers[0:7:3] = ['O'] * 3
        test_cube.faces[3].stickers[-3:] = ['G'] * 3
        test_cube.faces[4].stickers[2:9:3] = ['R'] * 3
        self.assertTrue(test_cube == new_cube)

        new_cube.moves.front(False)
        self.assertTrue(new_cube == self.cube)

    def test_back(self):
        """ TODO """
        pass

    def test_up(self):
        new_cube = Cube()
        new_cube.moves.left(False)
        new_cube.moves.right()
        new_cube.moves.up()
        test_cube = Cube()

        stickers = [
            ['B'] * 3 + 2 * ['R', 'W', 'R'],
            3 * ['Y', 'R', 'Y'],
            ['O', 'Y', 'O'] + 6 * ['B'],
            3 * ['W'] + 3 * ['O'] + 3 * ['W'],
            ['R', 'W', 'R'] + 6 * ['G'],
            2 * ['O', 'Y', 'O'] + 3 * ['G'],
        ]
        for idx in range(6):
            test_cube.faces[idx].stickers = stickers[idx]

        self.assertTrue(new_cube == test_cube)

        new_cube.moves.up(False)
        new_cube.moves.left()
        new_cube.moves.right(False)
        self.assertTrue(new_cube == self.cube)

    def test_down(self):
        new_cube = Cube()
        new_cube.moves.left(False)
        new_cube.moves.right()
        new_cube.moves.down()
        test_cube = Cube()

        stickers = [
            2 * ['R', 'W', 'R'] + 3 * ['G'],
            3 * ['Y'] + 3 * ['R'] + 3 * ['Y'],
            6 * ['B'] + ['R', 'W', 'R'],
            3 * ['W', 'O', 'W'],
            6 * ['G'] + ['O', 'Y', 'O'],
            3 * ['B'] + 2 * ['O', 'Y', 'O']
        ]
        for idx in range(6):
            test_cube.faces[idx].stickers = stickers[idx]

        self.assertTrue(new_cube == test_cube)

        new_cube.moves.down(False)
        new_cube.moves.left()
        new_cube.moves.right(False)
        self.assertTrue(new_cube == self.cube)

    def test_left(self):
        """ TODO """
        pass

    def test_right(self):
        """ TODO """
        pass

    def test__turn(self):
        """ TODO """
        pass

    def test_turn_down(self):
        """ TODO """
        pass

    def test_turn_up(self):
        """ TODO """
        pass

    def test_turn_left(self):
        """ TODO """
        pass

    def test_turn_right(self):
        """ TODO """
        pass

    def test_move_from_letter(self):
        """ TODO """
        pass

    def test_shuffle(self):
        """ TODO """
        pass