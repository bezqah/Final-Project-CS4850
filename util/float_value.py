from .value import Value

class FloatValue(Value):
    def __init__(self, val=None):
        self.val = val

    def add_value(self, val):
        self.val = val
        return self

    def getFloat(self):
        return float(self.val)

    def equals(self, v):
        return isinstance(v, FloatValue) and self.val == v.val

    def __str__(self):
        return str(self.val)
