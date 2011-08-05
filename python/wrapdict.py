class WrapDict():
    def __init__(self):
        self.d = {}

    def __length__(self):
        return len(self.d)

    def __getitem__(self, x):
        return self.d[x]

    def __setitem__(self, x, y):
        self.d[x] = y

    def __contains__(self, x):
        return x in self.d

    def items(self):
        return self.d.items()

    def keys(self):
        return self.d.keys()

    def get(self, key, default = None):
        return self.d.get(key, default)
