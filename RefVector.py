class RefVector:
    def __init__(self, x = 0, y = 0, rad = 0):
        self.x = x
        self.y = y
        self.rad = rad

    def __add__(self, right):
        return RefVector(self.x+right.x, self.y+right.y, self.rad+right.rad)
