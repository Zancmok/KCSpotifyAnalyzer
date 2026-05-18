FROM python:3.14-slim

ENV APP_VERSION="alpha-0.0.1"

WORKDIR /flask

COPY ./docker/flask/requirements.txt /flask/

RUN pip install --no-cache-dir -r /flask/requirements.txt

COPY ./src/ /flask/

COPY ./docker/flask/.env /flask/

EXPOSE 5000

CMD ["python", "main.py"]
