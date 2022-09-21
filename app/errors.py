import pydantic


class HttpError(Exception):
    def __init__(self, status_code: int, message: str | dict | list):
        self.status_code = status_code
        self.message = message


# Делаем класс для валидации данных
class CreateAnnounsment(pydantic.BaseModel):
    headline: str
    description: str
    owner: str



