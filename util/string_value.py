from .value import Value

class StringValue(Value):
    def __init__(self):
        self.val = None

    def __str__(self):
        return "'" + str(self.val) + "'"

    def add_value(self, val):
        self.val = val
        return self
    
    def get_label(self):
        return self.val

    def __eq__(self, other):
        return isinstance(other, StringValue) and self.val == other.val
