from flask import Flask, jsonify, request
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer

app = Flask('app')

Base = declarative_base()

class User(Base):

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)


@app.route('/test/', methods=['GET'])
def test():

    return jsonify({'status': 'OK'})


app.run()
