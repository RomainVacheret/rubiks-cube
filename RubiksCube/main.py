from display.Cube2DDisplay import Cube2DDisplay
from models.Cube import Cube

if __name__ == '__main__':
    cube = Cube()
    cube.faces[4].stickers[2] = 'Z'
    cube.faces[2].stickers[2] = 'Z'
    # cube.moves.right()
    # cube.moves.turnDown()

    cube.moves.up()
    cube.moves.turnLeft()
    cube.faces[4].stickers[2] = 'Z'
    cube.faces[2].stickers[2] = 'Z'
    cube.faces[3].stickers[2] = 'Z'
    cube.faces[1].stickers[2] = 'Z'
    
    # cube.faces[5].stickers = cube.faces[5].stickers[::-1]
    cubeDisplay = Cube2DDisplay(cube)
    cubeDisplay.display()

"""
    :TODO:
        - Rotate faces
"""