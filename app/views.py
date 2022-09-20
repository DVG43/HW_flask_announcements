import pydantic
from flask import jsonify, request
from flask.views import MethodView  # импорт базового класса для вьюх.
from db import Session
from models import Announsment
from errors import CreateAnnounsment, HttpError


def get_announsment(session: Session, announsment_id: int):  # получаем объявление.
    announsment = session.query(Announsment).get(announsment_id)
    if announsment is None:
        raise HttpError(404, 'announsment not found')
    return announsment


class AnnounView(MethodView):

    def get(self, announsment_id: int):
        with Session() as session:
            announ = get_announsment(session, announsment_id)
            return jsonify({'headline': announ.headline},
                           {'description': announ.description},
                           {'created_at': announ.created_at.isoformat()},
                           {'owner': announ.owner},)

    def post(self):
        try:
            validate = CreateAnnounsment(**request.json).dict()
        except pydantic.ValidationError as error:
            raise HttpError(400, error.errors())

        with Session() as session:
            announ = Announsment(headline=validate['headline'],
                                 description=validate['description'],
                                 owner=validate['owner'],
                                 )
            session.add(announ)
            session.commit()
            return {'id': announ.id}

    def delete(self, announsment_id: int):
        with Session() as session:
            announ = get_announsment(session, announsment_id)
            session.delete(announ)
            session.commit()
            return {'status': 'success deleting'}