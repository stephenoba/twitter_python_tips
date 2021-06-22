class PythonTipError(Exception):
    """
    A generic exception for all others to extend.
    """
    pass


class MissingAuthKey(PythonTipError):
    pass


class InvalidAuthKey(PythonTipError):
    pass
