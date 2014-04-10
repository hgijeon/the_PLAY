class RefVector:
    def __init__(self, left = 0, top = 0, rad = 0):
        self.top = top
        self.left = left
        self.rad = rad

        self.lt = (left, top)

    def __add__(self, right):
        return RefVector(self.left+right.left, self.top+right.top, self.rad+right.rad)
