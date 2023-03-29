from attr import dataclass

from src.Exceptions import ApiException


@dataclass(init=True)
class AuthException(ApiException):
    error: str
    code: int = 401
