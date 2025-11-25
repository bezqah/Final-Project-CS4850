from .value import Value

class VoidValue(Value):
    def __init__(self):
        self.val = None

    def __str__(self):
        return "#void"

    def __eq__(self, other):
        return isinstance(other, VoidValue)

    def add_value(self, val):
        return self
