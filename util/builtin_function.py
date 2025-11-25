from .function import Function

class BuiltinFunction(Function):
    def __str__(self):
        return "#builtin"
