class Moves:
    def __init__(self, cube):
        self.cube = cube

    def __faceInverser(self, index):
        self.cube.faces[index].stickers = self.cube.faces[index].stickers[::-1]

    def decorator(func):
        """ Decorator inversing back face before and after moving the cube. """
        def wrapper(*args, **kwargs):
            self = args[0]
            # self.cube.faces[5].stickers = self.cube.faces[5].stickers[::-1]
            self.__faceInverser(5)            
            result = func(*args, **kwargs)
            # self.cube.faces[5].stickers = self.cube.faces[5].stickers[::-1]
            self.__faceInverser(5)
            return result
        
        return wrapper

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
    
    def front(self, clockwiwe=True):
        """ Rotate the side facing the player. """
        self.cube.faces[0].frontMove(clockwiwe)

        if clockwiwe:
            self._swapTop(3, 4, 1, 2)
        else:
            tmp = self.cube.faces[3].stickers[:3]
            self._swapTop(3, 2, 1, 4)

    @decorator
    def up(self, clockwiwe=True):
        """ Rotate the side on top of the front side. """
        self.cube.faces[3].frontMove(clockwiwe)
        self.cube.faces[1].frontMove(not clockwiwe)

        if clockwiwe:
            self._swapTop(0, 4, 5, 2)
        else:
            self._swapTop(0, 2, 5, 4)
    
    @decorator
    def down(self, clockwiwe=True):
        """ Rotate the side underneath the cube. """
        self.cube.faces[1].frontMove(not clockwiwe)

        if clockwiwe:
            self._swapBot(0, 4, 5, 2)
        else:
            self._swapBot(0, 2, 5, 4)
        
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
        self.cube.faces[2].frontMove(not clockwiwe)

        if clockwiwe:
            self._swapRight(0, 3, 5, 1)
        else:
            self._swapRight(0, 1, 5, 3)

    def _turn(self, *faces):
        a, b, c, d = faces
        tmp = self.cube.faces[a]
        self.cube.faces[a] = self.cube.faces[b]
        self.cube.faces[b] = self.cube.faces[c]
        self.cube.faces[c] = self.cube.faces[d]
        self.cube.faces[d] = tmp

        # Maybe swap both
        # self.cube.faces[e].frontMove(False)
        # self.cube.faces[f].frontMove()
        
    def turnDown(self):
        """ Turns the whole cube to the bottom. """
        self._turn(0, 3, 5, 1)

        # self.cube.faces[2].stickers = self.cube.faces[2].stickers[::-1]
        # self.cube.faces[4].stickers = self.cube.faces[4].stickers[::-1]
        self.__faceInverser(2)
        self.__faceInverser(4)

        # self.cube.faces[2].frontMove(False)
        # self.cube.faces[4].frontMove()

    def turnUp(self):
        """ Turns the whole cube to the top. """
        self._turn(0, 1, 5, 3)

        # self.cube.faces[2].frontMove()
        # self.cube.faces[4].frontMove(False)

    def turnLeft(self):
        """ Turns the whole cube to the left. """
        # tmp = self.cube.faces[0]
        # self.cube.faces[0] = self.cube.faces[2]
        # self.cube.faces[2] = self.cube.faces[5]
        # self.cube.faces[5] = self.cube.faces[4]
        # self.cube.faces[4] = tmp
        self._turn(0, 2, 5, 4)

        self.__faceInverser(3)
        self.__faceInverser(1)

        # self.cube.faces[3].frontMove()
        # self.cube.faces[1].frontMove(False)
    
