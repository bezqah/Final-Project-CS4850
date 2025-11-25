from .value import Value
from .plp1_error import PLp1Error

class Function(Value):
    def __init__(self):
        super().__init__()

    def invoke(self, env, args):
        raise PLp1Error("invoke must be implemented by subclasses")
