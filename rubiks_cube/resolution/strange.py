class Strange:

    def ruru(self):
        return ('R', 'U', 'R\'', 'U\'')

    def lulu(self):
        return ('L\'', 'U\'', 'L', 'U')

    def right_hand(self):
        return 2 * self.ruru()
    
    def left_hand(self):
        return 2 * self.lulu()