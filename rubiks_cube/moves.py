import random
import warnings

from rubiks_cube.exceptions import (
    InvalidMoveException, 
    InvalidFacesException, 
    UnimplementedResourceException
)

""" TODO
    - Verify move 2 times is equal to invert for the 5th face
    - Faces combinations for swaps
    - Add exceptions to docstring
"""

def _face_invertion(cube, index):
    cube.faces[index].stickers = cube.faces[index].stickers[::-1]

def face_inverter(face_index):
        """ Decorator inversing given face before and after moving the cube. """
        def middle(func):
            def wrapper(*args, **kwargs):
                # args[0] represents `self` of the method of the Moves object 
                # in which the decorator is used
                cube = args[0].cube 
                _face_invertion(cube, face_index)            
                result = func(*args, **kwargs)
                _face_invertion(cube, face_index)
                return result
        
            return wrapper
        
        return middle

class Moves:
    LETTERS = ('R', 'R\'', 'L', 'L\'', 'B', 'B\'', 'D', 'D\'', 'F', 'F\'', 'U', 'U\'')

    def __init__(self, cube):
        self.cube = cube
    
    def _assert_faces_validity(self, faces):
        """ Asserts 4 faces are passed as argument. 
            :param faces: list which length must be asserted
            :type faces: List(Face)

            :raises InvalidFacesException: the length of the list is not equal to 4
        """
        INVALID_FACES_MSG = 'Four faces must be passed as arguments. \
        No duplicates are allowed and index must be within [0, 6['

        if len(faces) != 4:
            raise InvalidFacesException(INVALID_FACES_MSG)

    def _swap_top(self, *face_list):
        """ Swaps the fist row of each given face. """
        self._assert_faces_validity(face_list)

        a, b, c, d = face_list

        tmp = self.cube.faces[a].stickers[:3]
        self.cube.faces[a].stickers[:3] = self.cube.faces[b].stickers[:3]
        self.cube.faces[b].stickers[:3] = self.cube.faces[c].stickers[:3]
        self.cube.faces[c].stickers[:3] = self.cube.faces[d].stickers[:3]
        self.cube.faces[d].stickers[:3] = tmp
    
    def _swap_bot(self, *face_list):
        """ Swaps the last row of each given face. """
        self._assert_faces_validity(face_list)

        a, b, c, d = face_list

        tmp = self.cube.faces[a].stickers[-3:]
        self.cube.faces[a].stickers[-3:] = self.cube.faces[b].stickers[-3:]
        self.cube.faces[b].stickers[-3:] = self.cube.faces[c].stickers[-3:]
        self.cube.faces[c].stickers[-3:] = self.cube.faces[d].stickers[-3:]
        self.cube.faces[d].stickers[-3:] = tmp
    
    def _swap_left(self, *face_list):
        """ Swaps the left column of the front face. """
        self._assert_faces_validity(face_list)

        a, b, c, d = face_list

        tmp = self.cube.faces[a].stickers[::3]
        self.cube.faces[a].stickers[::3] = self.cube.faces[b].stickers[::3]
        self.cube.faces[b].stickers[::3] = self.cube.faces[c].stickers[::3]
        self.cube.faces[c].stickers[::3] = self.cube.faces[d].stickers[::3]
        self.cube.faces[d].stickers[::3] = tmp
    
    def _swap_right(self, *face_list):
        """ Swaps the right column of the front face. """
        self._assert_faces_validity(face_list)

        a, b, c, d = face_list

        tmp = self.cube.faces[a].stickers[2::3]
        self.cube.faces[a].stickers[2::3] = self.cube.faces[b].stickers[2::3]
        self.cube.faces[b].stickers[2::3] = self.cube.faces[c].stickers[2::3]
        self.cube.faces[c].stickers[2::3] = self.cube.faces[d].stickers[2::3]
        self.cube.faces[d].stickers[2::3] = tmp

    def mv_front_clockwise(self):
        self.cube.faces[0].rotate_clockwise()

        tmp = self.cube.faces[4].stickers[2::3]
        self.cube.faces[4].stickers[2::3] = self.cube.faces[1].stickers[:3]
        self.cube.faces[1].stickers[:3] = self.cube.faces[2].stickers[::3][::-1]
        self.cube.faces[2].stickers[::3] = self.cube.faces[3].stickers[-3:]
        self.cube.faces[3].stickers[-3:] = tmp[::-1]
    
    def mv_front_anti_clockwise(self):
        self.cube.faces[0].rotate_anti_clockwise()

        tmp = self.cube.faces[4].stickers[2::3]
        self.cube.faces[4].stickers[2::3] = self.cube.faces[3].stickers[-3:][::-1]
        self.cube.faces[3].stickers[-3:] = self.cube.faces[2].stickers[::3]
        self.cube.faces[2].stickers[::3] = self.cube.faces[1].stickers[:3][::-1]
        self.cube.faces[1].stickers[:3] = tmp
    
    def mv_back_clockwise(self):
        raise UnimplementedResourceException('B move has not yet been implemented.')
    
    def mv_back_anti_clockwise(self):
        raise UnimplementedResourceException('B\' move has not yet been implemented.')

    @face_inverter(5)
    def mv_up_clockwise(self):
        self.cube.faces[3].rotate_clockwise()
        self._swap_top(4, 0, 2, 5)
    
    @face_inverter(5)
    def mv_up_anti_clockwise(self):
        self.cube.faces[3].rotate_anti_clockwise()
        self._swap_top(4, 5, 2, 0)
    
    @face_inverter(5)
    def mv_down_clockwise(self):
        self._swap_bot(4, 5, 2, 0)
        self.cube.faces[1].rotate_clockwise()

    @face_inverter(5)
    def mv_down_anti_clockwise(self):
        self._swap_bot(4, 0, 2, 5)
        self.cube.faces[1].rotate_anti_clockwise()

    def mv_left_clockwise(self):
        self.cube.faces[4].rotate_clockwise()
        self._swap_left(0, 3, 5, 1)

    def mv_left_anti_clockwise(self):
        self.cube.faces[4].rotate_anti_clockwise()
        self._swap_left(0, 1, 5, 3)
    
    def mv_right_clockwise(self):
        self.cube.faces[2].rotate_clockwise()
        self._swap_right(0, 1, 5, 3)
    
    def mv_right_anti_clockwise(self):
        self.cube.faces[2].rotate_anti_clockwise()
        self._swap_right(0, 3, 5, 1)

    def _turn(self, *faces):
        a, b, c, d = faces
        tmp = self.cube.faces[a]
        self.cube.faces[a] = self.cube.faces[b]
        self.cube.faces[b] = self.cube.faces[c]
        self.cube.faces[c] = self.cube.faces[d]
        self.cube.faces[d] = tmp
        
    def turn_down(self):
        """ Turns the whole cube towards the bottom. """
        self.cube.faces[2].rotate_anti_clockwise()
        self.cube.faces[4].rotate_clockwise()

        self._turn(0, 3, 5, 1)

    def turn_up(self):
        """ Turns the whole cube towards the top. """
        self.cube.faces[2].rotate_clockwise()
        self.cube.faces[4].rotate_anti_clockwise()

        self._turn(0, 1, 5, 3)

    @face_inverter(5)
    def turn_left(self):
        """ Turns the whole cube towards the left. """
        self.cube.faces[3].rotate_clockwise()
        self.cube.faces[1].rotate_anti_clockwise()

        self._turn(0, 2, 5, 4)

    @face_inverter(5)
    def turn_right(self):
        """ Turns the whole cube towards the right. """
        self.cube.faces[3].rotate_anti_clockwise()
        self.cube.faces[1].rotate_clockwise()

        self.cube.faces[2].rotate_clockwise()
        self.cube.faces[2].rotate_clockwise()

        self._turn(0, 4, 5, 2)
    
    def _assert_move_validity(self, movement):
        if movement not in Moves.LETTERS:
            raise InvalidMoveException(f'{movement} is an incorrect move!')
    
    def move_from_letter(self, letter):
        self._assert_move_validity(letter)
        [
            self.mv_right_clockwise,
            self.mv_right_anti_clockwise,
            self.mv_left_clockwise,
            self.mv_left_anti_clockwise,
            self.mv_back_clockwise,
            self.mv_back_anti_clockwise,
            self.mv_down_clockwise,
            self.mv_down_anti_clockwise,
            self.mv_front_clockwise,
            self.mv_front_anti_clockwise,
            self.mv_up_clockwise,
            self.mv_up_anti_clockwise
        ][Moves.LETTERS.index(letter)]()
    
    def shuffle(self):
        """ Shuffles the cube. """
        turns = (
            self.turn_down,
            self.turn_up,
            self.turn_right,
            self.turn_left
        )
 
        for _ in range(100):
            move = random.randint(0, 15)
            if move < 12:
                self.move_from_letter('{}{}'.format(
                    self.LETTERS[move],
                    '' if random.randint(0, 1) else '\''
                ))
            else:
                turns[move - 12]()
