class  Rand48(object):
    def __init__(self, seed):
        self.seed = seed
        self.n = (seed << 16) + 0x330E


    def drand48(self):
        self.n = (0x5DEECE66D * self.n + 0XB) % (2**48)
        return self.n / (2**48)

    def seed(self):
        return self.seed
