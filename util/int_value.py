from .value import Value

class IntValue(Value):
    def __init__(self, v=None):
        super().__init__()
        if v is not None:
            self.val = v

    def add_value(self, val):
        self.val = val
        return self

    def get_int(self):
        return int(self.val)

    def __eq__(self, other):
        return isinstance(other, IntValue) and self.val == other.val

    def __str__(self):
        return str(self.val)
