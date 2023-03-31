from attr import dataclass

from src.Exceptions.Api import ApiException


@dataclass(init=True)
class AuthException(ApiException):
    error: str
    code: int = 401
