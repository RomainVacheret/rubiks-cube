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
        """ TODO """
        pass

    def test__swap_bot(self):
        """ TODO """
        pass

    def test__swap_left(self):
        """ TODO """
        pass

    def test__swap_right(self):
        """ TODO """
        pass

    def test_tmp(self):
        """ TODO """
        pass

    def test_front(self):
        """ TODO """
        pass

    def test_back(self):
        """ TODO """
        pass

    def test_up(self):
        """ TODO """
        pass

    def test_down(self):
        """ TODO """
        pass

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