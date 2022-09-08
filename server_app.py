import pydantic
from flask import Flask, jsonify, request
from flask.views import MethodView  # импорт базового класса для вьюх.
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import ( 
      Column, 
      Integer,
      DateTime,
      String,
      func,
      create_engine
)


# делаем класс ошибки
class HttpError(Exception):
    def __init__(self, status_code: int, message: str | dict | list):
        self.status_code = status_code
        self.message = message


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


PG_DSN = 'postgresql://dim43:1624@127.0.0.1:5431/for_flask'

engine = create_engine(PG_DSN)   # дключение к базе.
Session = sessionmaker(bind=engine)   # устраиваем рекурсию - откат

Base = declarative_base()


# создание модели
class Announsment(Base):

    __tablename__ = 'announsments'
    id = Column(Integer, primary_key=True)
    headline = Column(String(100), index=True, nullable=False)
    description = Column(String(200), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    owner = Column(String(50), nullable=False)


def get_announsment(session: Session, announsment_id: int):  # получаем объявление.
    announsment = session.query(Announsment).get(announsment_id)
    if announsment is None:
        raise HttpError(404, 'announsment not found')
    return announsment


Base.metadata.create_all(engine)


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


announ_view = AnnounView.as_view('announsments')
app.add_url_rule('/announsments/', view_func=announ_view, methods=['POST'])
app.add_url_rule('/announsments/<int:announsment_id>', view_func=announ_view, methods=['GET', 'DELETE'])


app.run()


# @app.route('/test/', methods=['GET'])
# def test():
#    return jsonify({'status': 'OK'})



