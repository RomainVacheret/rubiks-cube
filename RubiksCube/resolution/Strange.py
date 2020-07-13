class Strange:
    def __init__(self):
        pass

    def ruru(self):
        return ('R', 'U', 'R\'', 'U\'')

    def lulu(self):
        return ('L\'', 'U\'', 'L', 'U')

    def rightHand(self):
        return 2 * self.ruru()
    
    def leftHand(self):
        return 2 * self.lulu()