class PLp1Error(Exception):
    def __init__(self, message=None, cause=None):
        if cause is not None:
            super().__init__(message)
            self.__cause__ = cause
        else:
            super().__init__(message)

    def __str__(self):
        return self.args[0] if self.args else ""
