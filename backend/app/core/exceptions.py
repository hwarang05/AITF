"""
프로젝트 공통 예외

Service에서는 HTTPException 대신
프로젝트 공통 예외를 사용한다.
"""


class AppException(Exception):
    """
    프로젝트 기본 예외
    """

    status_code = 400

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class BadRequestException(AppException):
    status_code = 400


class UnauthorizedException(AppException):
    status_code = 401


class ForbiddenException(AppException):
    status_code = 403


class NotFoundException(AppException):
    status_code = 404


class ConflictException(AppException):
    status_code = 409
    