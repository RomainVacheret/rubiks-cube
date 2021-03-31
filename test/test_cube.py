import unittest

from rubiks_cube.exceptions import InvalidLineIndexException, InvalidLayerIndexException
from rubiks_cube.cube import Face, Cube, COLORS


class TestFace (unittest.TestCase):

    def _init_stickers(self):
        return (
            ['W', 'R', 'B', 'O', 'G', 'Y', 'G', 'O', 'B'],
            ['G', 'O', 'W', 'O', 'G', 'R', 'B', 'Y', 'B'],
            ['B', 'O', 'G', 'Y', 'G', 'O', 'B', 'R', 'W'],
            ['B', 'Y', 'B', 'R', 'G', 'O', 'W', 'O', 'G']
        )
    
    def _init_faces(self):
        new_face = Face(COLORS[0])
        new_face2 = Face(COLORS[0])
        new_face3 = Face(COLORS[0])
        new_face4 = Face(COLORS[0])

        stickers = self._init_stickers()

        new_face.stickers, \
        new_face2.stickers, \
        new_face3.stickers, \
        new_face4.stickers = stickers

        return new_face, new_face2, new_face3, new_face4
    
    def setUp(self):
        """ Creates a white face. """
        self.face = Face(COLORS[0])
        self.other_face = Face(COLORS[0])

    def test_is_completed(self):
        self.assertTrue(self.face.is_completed)

        self.face.stickers[0] = 'Y' 
        self.assertFalse(self.face.is_completed)
        self.face.stickers[0] =  'W' 

    def test_is_line_completed(self):
        with self.assertRaises(InvalidLineIndexException):
            self.face.line_is_completed(-1)
            self.face.line_is_completed(3)

        self.assertTrue(self.face.line_is_completed(0))
        self.assertTrue(self.face.line_is_completed(1))
        self.assertTrue(self.face.line_is_completed(2))

        self.face.stickers[0:7:3] = 'Y' * 3
        self.assertFalse(self.face.line_is_completed(0))
        self.assertFalse(self.face.line_is_completed(1))
        self.assertFalse(self.face.line_is_completed(2))
        self.face.stickers[0:7:3] = 'W' * 3

    def test_line_generator(self):
        merge_list = lambda list_: [element for line in list_ for element in line]

        stickers = self._init_stickers()[0]
        new_face = Face(COLORS[0])
        new_face.stickers = stickers
        new_list = merge_list(new_face.line_generator())
        self.assertTrue(stickers == new_list)

        merged_line = merge_list(self.face.line_generator())
        self.assertTrue(merged_line == ['W'] * 9)

        merged_line = merge_list(self.face.line_generator())
        self.assertFalse(merged_line == ['W'] * 8 + ['Y'])
    
    def test__front_move(self):
        s1, s2, s3 = self._init_stickers()[:3]

        result = Face.rotate_stickers(s1)
        self.assertEqual(result, s2)

        result = Face.rotate_stickers(result)
        self.assertEqual(result, s3)
    
    def test_move_clockwise(self):
        f1, f2, f3 = self._init_faces()[:3]

        f1.rotate_clockwise()
        self.assertTrue(f1 == f2)

        f1.rotate_clockwise()
        self.assertTrue(f1 == f3)
    
    def test_move_anti_clockwise(self):
        faces = list(self._init_faces())
        faces[1] = faces[-1]
        f1, f2, f3 = faces[:3]

        f1.rotate_anti_clockwise()
        self.assertTrue(f1 == f2)

        f1.rotate_anti_clockwise()
        self.assertTrue(f1 == f3)
    
    def test___eq__(self):
        self.assertTrue(self.face == self.other_face)

        self.other_face.stickers[4] = 'Y'
        self.assertFalse(self.face == self.other_face)
        self.other_face.stickers[4] = 'W'


class TestCube (unittest.TestCase):
    
    def setUp(self):
        self.cube = Cube()

    def test_is_completed(self):
        self.assertTrue(self.cube.is_completed)

        self.cube.faces[0].stickers[0] = 'Y'
        self.assertFalse(self.cube.is_completed)
        self.cube.faces[0].stickers[0] = 'W'

    def test_layer_is_completed(self):
        # TODO -> Finish
        with self.assertRaises(InvalidLayerIndexException):
            self.cube.layer_is_completed(-1)
            self.cube.layer_is_completed(3)
        
        for idx in range(3):
            self.assertTrue(self.cube.layer_is_completed(idx))

    def test___eq__(self):
        new_cube = Cube()
        self.assertTrue(new_cube == self.cube)
        
        new_cube.faces[0].stickers[0] = 'Y'
        self.assertFalse(new_cube == self.cube)
