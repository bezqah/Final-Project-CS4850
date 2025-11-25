from .value import Value

class BooleanValue(Value):
    def __init__(self):
        self.val = None

    def add_value(self, val):
        self.val = val
        return self

    def get_boolean(self):
        return bool(self.val)

    def equals(self, v):
        return isinstance(v, BooleanValue) and self.val == v.get()

    def __str__(self):
        return str(self.val)
