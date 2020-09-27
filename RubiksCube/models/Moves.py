import random
class Moves:
    LETTERS = ('R', 'L', 'U', 'F', 'D', 'B', 'X', 'Y')

    def __init__(self, cube):
        self.cube = cube

    def __faceInverser(self, index):
        self.cube.faces[index].stickers = self.cube.faces[index].stickers[::-1]

    def decorator(func):
        """ Decorator inversing back face before and after moving the cube. """
        def wrapper(*args, **kwargs):
            self = args[0]
            self.__faceInverser(5)            
            result = func(*args, **kwargs)
            self.__faceInverser(5)
            return result
        
        return wrapper

    # @decorator
    def _swapTop(self, *faceList):
        """ Swap the fist row of each given face. """
        assert len(faceList) == 4

        a, b, c, d = faceList

        tmp = self.cube.faces[a].stickers[:3]
        self.cube.faces[a].stickers[:3] = self.cube.faces[b].stickers[:3]
        self.cube.faces[b].stickers[:3] = self.cube.faces[c].stickers[:3]
        self.cube.faces[c].stickers[:3] = self.cube.faces[d].stickers[:3]
        self.cube.faces[d].stickers[:3] = tmp
    
    def _swapBot(self, *faceList):
        """ Swap the fist row of each given face. """
        assert len(faceList) == 4

        a, b, c, d = faceList

        tmp = self.cube.faces[a].stickers[-3:]
        self.cube.faces[a].stickers[-3:] = self.cube.faces[b].stickers[-3:]
        self.cube.faces[b].stickers[-3:] = self.cube.faces[c].stickers[-3:]
        self.cube.faces[c].stickers[-3:] = self.cube.faces[d].stickers[-3:]
        self.cube.faces[d].stickers[-3:] = tmp
    
    def _swapLeft(self, *faceList):
        """ Swap the left column of the front face. """
        assert len(faceList) == 4

        a, b, c, d = faceList

        tmp = self.cube.faces[a].stickers[::3]
        self.cube.faces[a].stickers[::3] = self.cube.faces[b].stickers[::3]
        self.cube.faces[b].stickers[::3] = self.cube.faces[c].stickers[::3]
        self.cube.faces[c].stickers[::3] = self.cube.faces[d].stickers[::3]
        self.cube.faces[d].stickers[::3] = tmp
    
    def _swapRight(self, *faceList):
        """ Swap the right column of the front face. """
        assert len(faceList) == 4

        a, b, c, d = faceList

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
        self.cube.faces[0].frontMove(clockwise)

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

        self.cube.faces[3].frontMove(clockwise)

        if clockwise:
            self._swapTop(4, 0, 2, 5)
        else:
            self._swapTop(4, 5, 2, 0)
    
    # @decorator
    def down(self, clockwiwe=True):
        """ Rotate the side underneath the cube. """
        self.cube.faces[1].frontMove(clockwiwe)

        if clockwiwe:
            self._swapBot(4, 5, 2, 0)
        else:
            self._swapBot(4, 0, 2, 5)
        
    # @decorator
    def left(self, clockwiwe=True):
        """ Rotate the side to the left of the cube."""
        self.cube.faces[4].frontMove(clockwiwe)

        if clockwiwe:
            self._swapLeft(0, 3, 5, 1)
        else:
            self._swapLeft(0, 1, 5, 3)

    # @decorator
    def right(self, clockwiwe=True):
        """ Rotate the side to the right of the cube."""
        self.cube.faces[2].frontMove(clockwiwe)

        if clockwiwe:
            self._swapRight(0, 1, 5, 3)
            
        else:
            self._swapRight(0, 3, 5, 1)

    def _turn(self, *faces):
        a, b, c, d = faces
        tmp = self.cube.faces[a]
        self.cube.faces[a] = self.cube.faces[b]
        self.cube.faces[b] = self.cube.faces[c]
        self.cube.faces[c] = self.cube.faces[d]
        self.cube.faces[d] = tmp
        
    def turnDown(self):
        """ Turns the whole cube to the bottom. """
        self.cube.faces[2].frontMove(False)
        self.cube.faces[4].frontMove()

        self._turn(0, 3, 5, 1)

    def turnUp(self):
        """ Turns the whole cube to the top. """
        self.cube.faces[2].frontMove()
        self.cube.faces[4].frontMove(False)

        self._turn(0, 1, 5, 3)

    @decorator
    def turnLeft(self):
        """ Turns the whole cube to the left. """
        self.cube.faces[3].frontMove()
        self.cube.faces[1].frontMove(False)

        self._turn(0, 2, 5, 4)

    @decorator
    def turnRight(self):
        """ Turns the whole cube to the right. """
        self.cube.faces[3].frontMove(False)
        self.cube.faces[1].frontMove()

        self.cube.faces[2].frontMove()
        self.cube.faces[2].frontMove()

        self._turn(0, 4, 5, 2)
    
    def moveFromLetter(self, letter):
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
            raise Exception('Unvalid move!')

        # The cube is turned
        if index > 5:
            turns = (
                self.turnRight, 
                self.turnLeft, 
                self.turnDown, 
                self.turnUp, 
            )
            newIndex = index - 6 + (index == 7) + (length == 2)
            turns[newIndex]()
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
            self.turnDown,
            self.turnUp,
            self.turnRight,
            self.turnLeft
        )
 
        for _ in range(100):
            move = random.randint(0, 10)
            if move < 7:
                self.moveFromLetter('{}{}'.format(
                    self.LETTERS[move],
                    '' if random.randint(0, 1) else '\''
                ))
            else:
                self.turns[move - 7]()

"""
Verify move 2 times is equal to invert for the 5th face
"""

        
    
