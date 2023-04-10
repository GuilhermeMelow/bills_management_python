from dataclasses import dataclass

from src.Exceptions.Api import ApiException


@dataclass(frozen=True)
class AuthException(ApiException):
    error: str
    code: int = 401
