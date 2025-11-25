class Value:
    def __init__(self):
        self.val = None

    def get(self):
        return self.val

    def set(self, val):
        self.val = val

    def add_value(self, val):
        raise NotImplementedError("add_value must be implemented by subclasses")

    def __str__(self):
        raise NotImplementedError("__str__ must be implemented by subclasses")
