import pydantic
from flask import Flask, jsonify


class HttpError(Exception):
    def __init__(self, status_code: int, message: str | dict | list):
        self.status_code = status_code
        self.message = message


# Делаем класс для валидации данных
class CreateAnnounsment(pydantic.BaseModel):
    headline: str
    description: str
    owner: str


app = Flask('app')


@app.errorhandler(HttpError)
def http_error_handler(error: HttpError):
    response = jsonify({
           'status': 'error',
           'reason': error.message
    })
    response.status_code = error.status_code
       return response