

class ApiException(Exception):
    error: str
    code: int
