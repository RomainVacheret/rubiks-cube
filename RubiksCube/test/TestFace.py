# import unittest
# from RubiksCube.models.Face import Face

# # from models.Face import Face

# class TestFace(unittest.TestCase):
#     # def __init__(self):
#     #     super().__init__()
#     #     self.face = Face('W')
#     face = Face('W')

#     def testIsCompleted(self):
#         self.assertTrue(self.face.isCompleted)

#         self.face.stickers[0] = 'B'
#         self.assertFalse(self.face.isCompleted)
#         self.face.stickers[0] = 'W'

#         self.face.frontMove()
#         self.assertFalse(self.face.isCompleted)
    
#     def testLineIsCompleted(self):
#         for index in range(3):
#             self.assertTrue(self.face.lineIsCompleted(index))

        
#         self.face.stickers[4] = 'B'
#         self.assertTrue(self.face.lineIsCompleted(0))
#         self.assertFalse(self.face.lineIsCompleted(1))
#         self.assertTrue(self.face.lineIsCompleted(2))


# if __name__ == '__main__':
#     unittest.main()