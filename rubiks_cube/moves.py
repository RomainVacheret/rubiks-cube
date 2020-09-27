import random

from .exceptions import UnValidMoveException

class Moves:
    LETTERS = ('R', 'L', 'U', 'F', 'D', 'B', 'X', 'Y')

    def __init__(self, cube):
        self.cube = cube

    def __face_inverser(self, index):
        self.cube.faces[index].stickers = self.cube.faces[index].stickers[::-1]

    def decorator(func):
        """ Decorator inversing back face before and after moving the cube. """
        def wrapper(*args, **kwargs):
            self = args[0]
            self.__face_inverser(5)            
            result = func(*args, **kwargs)
            self.__face_inverser(5)
            return result
        
        return wrapper

    # @decorator
    def _swap_top(self, *face_list):
        """ Swap the fist row of each given face. """
        assert len(face_list) == 4

        a, b, c, d = face_list

        tmp = self.cube.faces[a].stickers[:3]
        self.cube.faces[a].stickers[:3] = self.cube.faces[b].stickers[:3]
        self.cube.faces[b].stickers[:3] = self.cube.faces[c].stickers[:3]
        self.cube.faces[c].stickers[:3] = self.cube.faces[d].stickers[:3]
        self.cube.faces[d].stickers[:3] = tmp
    
    def _swap_bot(self, *face_list):
        """ Swap the fist row of each given face. """
        assert len(face_list) == 4

        a, b, c, d = face_list

        tmp = self.cube.faces[a].stickers[-3:]
        self.cube.faces[a].stickers[-3:] = self.cube.faces[b].stickers[-3:]
        self.cube.faces[b].stickers[-3:] = self.cube.faces[c].stickers[-3:]
        self.cube.faces[c].stickers[-3:] = self.cube.faces[d].stickers[-3:]
        self.cube.faces[d].stickers[-3:] = tmp
    
    def _swap_left(self, *face_list):
        """ Swap the left column of the front face. """
        assert len(face_list) == 4

        a, b, c, d = face_list

        tmp = self.cube.faces[a].stickers[::3]
        self.cube.faces[a].stickers[::3] = self.cube.faces[b].stickers[::3]
        self.cube.faces[b].stickers[::3] = self.cube.faces[c].stickers[::3]
        self.cube.faces[c].stickers[::3] = self.cube.faces[d].stickers[::3]
        self.cube.faces[d].stickers[::3] = tmp
    
    def _swap_right(self, *face_list):
        """ Swap the right column of the front face. """
        assert len(face_list) == 4

        a, b, c, d = face_list

        tmp = self.cube.faces[a].stickers[2::3]
        self.cube.faces[a].stickers[2::3] = self.cube.faces[b].stickers[2::3]
        self.cube.faces[b].stickers[2::3] = self.cube.faces[c].stickers[2::3]
        self.cube.faces[c].stickers[2::3] = self.cube.faces[d].stickers[2::3]
        self.cube.faces[d].stickers[2::3] = tmp

    def tmp(self, *faces):
        a, b, c, d = faces
        tmp = self.cube.faces[4].stickers[2::3]
        self.cube.faces[4].stickers[2::3] = self.cube.faces[1].stickers[:3]
        self.cube.faces[1].stickers[:3] = self.cube.faces[2].stickers[0::3]
        self.cube.faces[2].stickers[0::3] = self.cube.faces[3].stickers[-3:]
        self.cube.faces[3].stickers[-3:] = tmp
    
    def front(self, clockwise=True):
        """ Rotate the side facing the player. """
        self.cube.faces[0].front_move(clockwise)

        if clockwise:
            tmp = self.cube.faces[4].stickers[2::3]
            self.cube.faces[4].stickers[2::3] = self.cube.faces[1].stickers[:3]
            self.cube.faces[1].stickers[:3] = self.cube.faces[2].stickers[::3][::-1]
            self.cube.faces[2].stickers[::3] = self.cube.faces[3].stickers[-3:]
            self.cube.faces[3].stickers[-3:] = tmp[::-1]
        else:

            tmp = self.cube.faces[4].stickers[2::3]
            self.cube.faces[4].stickers[2::3] = self.cube.faces[3].stickers[-3:][::-1]
            self.cube.faces[3].stickers[-3:] = self.cube.faces[2].stickers[::3]
            self.cube.faces[2].stickers[::3] = self.cube.faces[1].stickers[:3][::-1]
            self.cube.faces[1].stickers[:3] = tmp

    
    def back(self, clockwise):
        raise Exception('TODO')


    @decorator
    def up(self, clockwise=True):
        """ Rotate the side on top of the front side. """

        self.cube.faces[3].front_move(clockwise)

        if clockwise:
            self._swap_top(4, 0, 2, 5)
        else:
            self._swap_top(4, 5, 2, 0)
    
    # @decorator
    def down(self, clockwiwe=True):
        """ Rotate the side underneath the cube. """
        self.cube.faces[1].front_move(clockwiwe)

        if clockwiwe:
            self._swap_bot(4, 5, 2, 0)
        else:
            self._swap_bot(4, 0, 2, 5)
        
    # @decorator
    def left(self, clockwiwe=True):
        """ Rotate the side to the left of the cube."""
        self.cube.faces[4].front_move(clockwiwe)

        if clockwiwe:
            self._swap_left(0, 3, 5, 1)
        else:
            self._swap_left(0, 1, 5, 3)

    # @decorator
    def right(self, clockwiwe=True):
        """ Rotate the side to the right of the cube."""
        self.cube.faces[2].front_move(clockwiwe)

        if clockwiwe:
            self._swap_right(0, 1, 5, 3)
            
        else:
            self._swap_right(0, 3, 5, 1)

    def _turn(self, *faces):
        a, b, c, d = faces
        tmp = self.cube.faces[a]
        self.cube.faces[a] = self.cube.faces[b]
        self.cube.faces[b] = self.cube.faces[c]
        self.cube.faces[c] = self.cube.faces[d]
        self.cube.faces[d] = tmp
        
    def turn_down(self):
        """ Turns the whole cube to the bottom. """
        self.cube.faces[2].front_move(False)
        self.cube.faces[4].front_move()

        self._turn(0, 3, 5, 1)

    def turn_up(self):
        """ Turns the whole cube to the top. """
        self.cube.faces[2].front_move()
        self.cube.faces[4].front_move(False)

        self._turn(0, 1, 5, 3)

    @decorator
    def turn_left(self):
        """ Turns the whole cube to the left. """
        self.cube.faces[3].front_move()
        self.cube.faces[1].front_move(False)

        self._turn(0, 2, 5, 4)

    @decorator
    def turn_right(self):
        """ Turns the whole cube to the right. """
        self.cube.faces[3].front_move(False)
        self.cube.faces[1].front_move()

        self.cube.faces[2].front_move()
        self.cube.faces[2].front_move()

        self._turn(0, 4, 5, 2)
    
    def move_from_letter(self, letter):
        """ Executes the move linked to the given letter. """
        print(letter)
        try:
            index = self.LETTERS.index(letter[0])
        except ValueError as e:
            raise e

        length = len(letter)
        if length == 2:
            assert letter.endswith('\'')
        elif length > 2:
            raise UnValidMoveException()

        # The cube is turned
        if index > 5:
            turns = (
                self.turn_right, 
                self.turn_left, 
                self.turn_down, 
                self.turn_up, 
            )
            new_index = index - 6 + (index == 7) + (length == 2)
            turns[new_index]()
        # Move made on the main face (nb 0)
        else:
            moves = (
                self.right,
                self.left,
                self.up,
                self.front,
                self.down,
                self.back
            )

            moves[index](length == 1)
    
    def shuffle(self):
        """ Shuffle the cube. """
        turns = (
            self.turn_down,
            self.turn_up,
            self.turn_right,
            self.turn_left
        )
 
        for _ in range(100):
            move = random.randint(0, 10)
            if move < 7:
                self.move_from_letter('{}{}'.format(
                    self.LETTERS[move],
                    '' if random.randint(0, 1) else '\''
                ))
            else:
                self.turns[move - 7]()

"""
Verify move 2 times is equal to invert for the 5th face
"""

        
    
