import unittest

from rubiks_cube.cube import Cube, Face
from rubiks_cube.moves import _face_invertion, face_inverter, Moves
from rubiks_cube.exceptions import InvalidFacesException, InvalidMoveException

class TestFunctions(unittest.TestCase):
    def test__face_inverter(self):
        cube = Cube()
        cube.faces[0].stickers = ['W', 'R', 'B', 'O', 'G', 'Y', 'G', 'O', 'B']
        _face_invertion(cube, 0)
        self.assertTrue(cube.faces[0].stickers == ['B', 'O', 'G', 'Y', 'G', 'O', 'B', 'R', 'W'])

    def test_face_inerter(self):
        """ TODO """
        pass

class TestMoves(unittest.TestCase):
    
    def setUp(self):
        self.cube = Cube()
        self.moves = Moves(self.cube)
    
    def test__assert_faces_validity(self):
        first_list = [Face('ORANGE'), Face('WHITE')]
        second_list = [Face('ORANGE'), Face('WHITE'), Face('BLUE'), Face('YELLOW')]
        third_list = [Face('ORANGE'), Face('WHITE'), Face('BLUE'), Face('YELLOW'), Face('RED')]
        fourth_list = []

        with self.assertRaises(InvalidFacesException):
            self.moves._assert_faces_validity(first_list)
            self.moves._assert_faces_validity(third_list)
            self.moves._assert_faces_validity(fourth_list)

        self.moves._assert_faces_validity(second_list)
    
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

    def _init_front_cube(self):
        cube = Cube()
        cube.faces[1].stickers[:3] = ['B'] * 3
        cube.faces[2].stickers[0:7:3] = ['O'] * 3
        cube.faces[3].stickers[-3:] = ['G'] * 3
        cube.faces[4].stickers[2:9:3] = ['R'] * 3

        return cube

    def test_mv_front_clockwise(self):
        cube = self._init_front_cube()
        test_cube = Cube()
        test_cube.moves.mv_front_clockwise()

        self.assertEqual(test_cube, cube)
    
    def test_mv_front_anti_clockwise(self):
        cube = Cube()
        test_cube = self._init_front_cube()
        test_cube.moves.mv_front_anti_clockwise()

        self.assertEqual(test_cube, cube)

    def test_back(self):
        """ TODO """
        pass
    
    def _init_cube(self):
        cube = Cube()
        stickers = [
            ['W', 'Y', 'W', 'Y', 'W', 'Y', 'W', 'Y', 'W'],
            ['R', 'O', 'R', 'O', 'R', 'O', 'R', 'O', 'R'],
            ['B', 'G', 'B', 'G', 'B', 'G', 'B', 'G', 'B'],
            ['O', 'R', 'O', 'R', 'O', 'R', 'O', 'R', 'O'],
            ['G', 'B', 'G', 'B', 'G', 'B', 'G', 'B', 'G'],
            ['Y', 'W', 'Y', 'W', 'Y', 'W', 'Y', 'W', 'Y']
        ]

        for idx in range(6):
            cube.faces[idx].stickers = stickers[idx]

        return cube
    
    def test_mv_up_clockwise(self):
        cube = self._init_cube()
        cube.faces[0].stickers[:3] = ['B', 'G', 'B']
        cube.faces[2].stickers[:3] = ['Y', 'W', 'Y']
        cube.faces[4].stickers[:3] = ['W', 'Y', 'W']
        cube.faces[5].stickers[-3:] = ['G', 'B', 'G']
        test_cube = self._init_cube()

        test_cube.moves.mv_up_clockwise()

        self.assertEqual(test_cube, cube)
    
    def test_mv_up_anti_clockwise(self):
        cube = self._init_cube()
        test_cube = self._init_cube()
        test_cube.faces[0].stickers[:3] = ['B', 'G', 'B']
        test_cube.faces[2].stickers[:3] = ['Y', 'W', 'Y']
        test_cube.faces[4].stickers[:3] = ['W', 'Y', 'W']
        test_cube.faces[5].stickers[-3:] = ['G', 'B', 'G']

        test_cube.moves.mv_up_anti_clockwise()

        self.assertEqual(test_cube, cube)
    
    def test_mv_down_clockwise(self):
        cube = self._init_cube()
        cube.faces[0].stickers[-3:] = ['G', 'B', 'G']
        cube.faces[2].stickers[-3:] = ['W', 'Y', 'W']
        cube.faces[4].stickers[-3:] = ['Y', 'W', 'Y']
        cube.faces[5].stickers[:3] = ['B', 'G', 'B']
        test_cube = self._init_cube()

        test_cube.moves.mv_down_clockwise()
        self.assertEqual(test_cube, cube)
    
    def test_mv_down_anti_clockwise(self):
        cube = self._init_cube()
        test_cube = self._init_cube()
        test_cube.faces[0].stickers[-3:] = ['G', 'B', 'G']
        test_cube.faces[2].stickers[-3:] = ['W', 'Y', 'W']
        test_cube.faces[4].stickers[-3:] = ['Y', 'W', 'Y']
        test_cube.faces[5].stickers[:3] = ['B', 'G', 'B']

        test_cube.moves.mv_down_anti_clockwise()
        self.assertEqual(test_cube, cube)
    
    def test_mv_left_clockwise(self):
        cube = self._init_cube()
        cube.faces[0].stickers[0:7:3] = ['O', 'R', 'O']
        cube.faces[1].stickers[0:7:3] = ['W', 'Y', 'W']
        cube.faces[3].stickers[0:7:3] = ['Y', 'W', 'Y']
        cube.faces[5].stickers[0:7:3] = ['R', 'O', 'R']
        test_cube = self._init_cube()

        test_cube.moves.mv_left_clockwise()

        self.assertEqual(test_cube, cube)
    
    def test_mv_left_anti_clockwise(self):
        cube = self._init_cube()
        cube.faces[0].stickers[0:7:3] = ['R', 'O', 'R']
        cube.faces[1].stickers[0:7:3] = ['Y', 'W', 'Y']
        cube.faces[3].stickers[0:7:3] = ['W', 'Y', 'W']
        cube.faces[5].stickers[0:7:3] = ['O', 'R', 'O']
        test_cube = self._init_cube()

        test_cube.moves.mv_left_anti_clockwise()

        self.assertEqual(test_cube, cube)
    
    def test_mv_right_clockwise(self):
        cube = self._init_cube()
        cube.faces[0].stickers[2:9:3] = ['R', 'O', 'R']
        cube.faces[1].stickers[2:9:3] = ['Y', 'W', 'Y']
        cube.faces[3].stickers[2:9:3] = ['W', 'Y', 'W']
        cube.faces[5].stickers[2:9:3] = ['O', 'R', 'O']
        test_cube = self._init_cube()

        test_cube.moves.mv_right_clockwise()

        self.assertEqual(test_cube, cube)
    
    def test_mv_right_anti_clockwise(self):
        cube = self._init_cube()
        cube.faces[0].stickers[2:9:3] = ['O', 'R', 'O']
        cube.faces[1].stickers[2:9:3] = ['W', 'Y', 'W']
        cube.faces[3].stickers[2:9:3] = ['Y', 'W', 'Y']
        cube.faces[5].stickers[2:9:3] = ['R', 'O', 'R']
        test_cube = self._init_cube()

        test_cube.moves.mv_right_anti_clockwise()

        self.assertEqual(test_cube, cube)

    def _prepare_cube(self, cube):
        cube.moves.mv_up_anti_clockwise()
        cube.moves.mv_down_anti_clockwise()
        cube.moves.mv_right_anti_clockwise()
        cube.moves.mv_up_clockwise()
        cube.moves.mv_front_clockwise()

    def test__turn(self):
        # TODO -> improve
        new_cube = Cube()
        faces = new_cube.faces
        new_faces = [
            faces[2],
            faces[1],
            faces[5],
            faces[3],
            faces[0],
            faces[4]
        ]
        new_cube.faces = new_faces

        test_cube = Cube()
        test_cube.moves._turn(0, 2, 5, 4)

        self.assertTrue(test_cube == new_cube)

    def test_turn_down(self):
        # TODO -> improve
        def swap_faces(cube):
            faces = cube.faces
            new_faces = [
                faces[3],
                faces[0],
                faces[2],
                faces[5],
                faces[4],
                faces[1]
            ]
            cube.faces = new_faces

        # Simple test
        new_cube = Cube()
        swap_faces(new_cube)
        
        test_cube = Cube()
        test_cube.moves.turn_down()

        self.assertTrue(test_cube == new_cube)

        # Complexe test
        new_cube = Cube()
        self._prepare_cube(new_cube)

        swap_faces(new_cube)
        new_cube.faces[4].rotate_clockwise()
        new_cube.faces[2].rotate_anti_clockwise()
        
        test_cube = Cube()
        self._prepare_cube(test_cube)
        test_cube.moves.turn_down()

        self.assertTrue(test_cube == new_cube)

    def test_turn_up(self):
        # TODO -> improve
        def swap_faces(cube):
            faces = cube.faces
            new_faces = [
                faces[1],
                faces[5],
                faces[2],
                faces[0],
                faces[4],
                faces[3]
            ]
            cube.faces = new_faces

        # Simple test
        new_cube = Cube()
        swap_faces(new_cube)
        
        test_cube = Cube()
        test_cube.moves.turn_up()

        self.assertTrue(test_cube == new_cube)

        # Complexe test
        new_cube = Cube()
        self._prepare_cube(new_cube)

        swap_faces(new_cube)
        new_cube.faces[4].rotate_anti_clockwise()
        new_cube.faces[2].rotate_clockwise()

        test_cube = Cube()
        self._prepare_cube(test_cube)
        test_cube.moves.turn_up()

        self.assertTrue(test_cube == new_cube)

    def test_turn_left(self):
        # TODO -> improve
        # Simple test
        new_cube = Cube()
        faces = new_cube.faces
        new_faces = [
            faces[2],
            faces[1],
            faces[5],
            faces[3],
            faces[0],
            faces[4]
        ]
        new_cube.faces = new_faces
        
        test_cube = Cube()
        test_cube.moves.turn_left()

        self.assertTrue(test_cube == new_cube)

        # Complexe test
        # new_cube = Cube()
        # self._prepare_cube(new_cube)

        # test_cube = Cube()
        # self._prepare_cube(test_cube)

        # faces = new_cube.faces
        # new_faces = [
        #     faces[2],
        #     faces[1],
        #     faces[5],
        #     faces[3],
        #     faces[0],
        #     faces[4]
        # ]

        # new_cube.faces = new_faces
        # new_cube.faces[1].rotate_anti_clockwise()
        # new_cube.faces[3].rotate_clockwise()
        
        # test_cube.moves.turn_left()

        # # Decorator used

        # print()
        # print(test_cube)
        # print(new_cube)

        # self.assertTrue(test_cube == new_cube)

    def test_turn_right(self):
        # TODO -> improve
        new_cube = Cube()
        faces = new_cube.faces
        new_faces = [
            faces[4],
            faces[1],
            faces[0],
            faces[3],
            faces[5],
            faces[2]
        ]
        new_cube.faces = new_faces
        
        test_cube = Cube()
        test_cube.moves.turn_right()

        self.assertTrue(test_cube == new_cube)
    
    def test__assert_move_validity(self):
        for move in Moves.LETTERS:
            self.moves._assert_move_validity(move)
        
        with self.assertRaises(InvalidMoveException):
            self.moves.move_from_letter('A')
            self.moves.move_from_letter('')
            self.moves.move_from_letter('F\'\'')
            self.moves.move_from_letter('B\'\'')

    def test_move_from_letter(self):
        # TODO -> add back
        cube = self._init_cube()
        cube_right = self._init_cube()
        cube_right.faces[0].stickers[2:9:3] = ['R', 'O', 'R']
        cube_right.faces[1].stickers[2:9:3] = ['Y', 'W', 'Y']
        cube_right.faces[3].stickers[2:9:3] = ['W', 'Y', 'W']
        cube_right.faces[5].stickers[2:9:3] = ['O', 'R', 'O']
        cube_left = self._init_cube()
        cube_left.faces[0].stickers[0:7:3] = ['O', 'R', 'O']
        cube_left.faces[1].stickers[0:7:3] = ['W', 'Y', 'W']
        cube_left.faces[3].stickers[0:7:3] = ['Y', 'W', 'Y']
        cube_left.faces[5].stickers[0:7:3] = ['R', 'O', 'R']
        cube_up = self._init_cube()
        cube_up.faces[0].stickers[:3] = ['B', 'G', 'B']
        cube_up.faces[2].stickers[:3] = ['Y', 'W', 'Y']
        cube_up.faces[4].stickers[:3] = ['W', 'Y', 'W']
        cube_up.faces[5].stickers[-3:] = ['G', 'B', 'G']
        cube_down = self._init_cube()
        cube_down.faces[0].stickers[-3:] = ['G', 'B', 'G']
        cube_down.faces[2].stickers[-3:] = ['W', 'Y', 'W']
        cube_down.faces[4].stickers[-3:] = ['Y', 'W', 'Y']
        cube_down.faces[5].stickers[:3] = ['B', 'G', 'B']
        test_cube = self._init_cube()

        test_cube.moves.move_from_letter('R')
        self.assertEqual(test_cube, cube_right)
        test_cube.moves.move_from_letter('R\'')
        self.assertEqual(test_cube, cube)
        test_cube.moves.move_from_letter('L')
        self.assertEqual(test_cube, cube_left)
        test_cube.moves.move_from_letter('L\'')
        self.assertEqual(test_cube, cube)
        test_cube.moves.move_from_letter('U')
        self.assertEqual(test_cube, cube_up)
        test_cube.moves.move_from_letter('U\'')
        self.assertEqual(test_cube, cube)
        test_cube.moves.move_from_letter('D')
        self.assertEqual(test_cube, cube_down)
        test_cube.moves.move_from_letter('D\'')
        self.assertEqual(test_cube, cube)

    def test_shuffle(self):
        """ TODO """
        pass