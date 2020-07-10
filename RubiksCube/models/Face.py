class Face:
    """ Represents a Rubik's cube face which is 
        composed of 9 stickers. 
        To complete a face each sticker must have the same 
        color.
        
    """
    def __init__(self, color):
        self.stickers = [color[0] for _ in range(9)]

    @property
    def color(self):
        """ Reprensents the starting color of the face. """
        # the 4th index is the center (which never changes)
        return self.stickers[4]

    @property
    def isCompleted(self):
        """ Informs if each face is completed. """
        return all(sticker == self.color for sticker in self.stickers)

    def lineIsCompleted(self, index):
        """ Check if all three sticker of sticker line are of the 
            same color. 
            Note that the color must be the face's color. 
            
            :param index: Line index between 0 included and 3 excluded.
            :type index: int
            
            :return: The color of each sticker is the same or not.
            :rtype: bool
        """
        assert 0 <= index < 3
        startingIndex = index * 3
        color = self.stickers[startingIndex]
        return self.stickers[startingIndex:startingIndex + 3] \
            .count(color) == 3 and color == self.color

    def lineGenerator(self):
        """ Yields each line of the current face. """
        for index in range(0, 9, 3):
            yield self.stickers[index:index+3]
    
    def frontMove(self, clockwise=True):
        """ Rotates the current face.
            
            :param clockwise: Clockwise or anticlockwise rotation.
            :type clockwise: bool
        """
        new = []
        idx = 6
        for _ in range(3):
            for i in range(3):
                new.append(self.stickers[idx - (3 * i)])
            idx += 1

        self.stickers = new if clockwise else new[::-1]


if __name__ == '__main__':
    face = Face('RED')
    # face.stickers[0] = 'BLUE'
    # for i in range(3):
    #     print(face.lineIsCompleted(i))
    face.stickers = list(range(9))
    face.frontMove(False)
    for a in face.lineGenerator():
        print(a)