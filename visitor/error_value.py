from util.value import Value

class ErrorValue(Value):
    def add_value(self, val: str):
        self.set(val)
        return self

    def __str__(self):
        return str(self.get())
