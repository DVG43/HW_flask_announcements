FROM python:3.10
COPY . /src
COPY . /requirements.txt/src/requirements.txt

WORKDIR /src

RUN pip install --no-cache-dir -r /src/requirements.txt

CMD ["python3", "run.py", "makemigrations"]
CMD ["python3", "run.py", "migrate"]
CMD ["python3", "run.py", "runserver"]