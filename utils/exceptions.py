class AppException(Exception):
    pass

class NotFoundException(AppException):
    def __init__(self, name: str):
        super().__init__(f"{name} not found")
