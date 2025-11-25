from .plp1_error import PLp1Error

class NoVariableDefError(PLp1Error):
    def __init__(self, message=None, cause=None):
        if message is not None and cause is not None:
            super().__init__(f"{message}: {cause}")
        elif message is not None:
            super().__init__(message)
        elif cause is not None:
            super().__init__(str(cause))
        else:
            super().__init__()
