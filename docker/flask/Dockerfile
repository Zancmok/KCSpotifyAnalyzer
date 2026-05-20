FROM node:26-slim AS ts-build

WORKDIR /ts

RUN npm install -g typescript

COPY ./src/static/script/ /script/

RUN tsc -p /script/ --rootDir /script --outDir /ts/script


FROM python:3.14-slim AS py-build

ENV APP_VERSION="alpha-0.0.2"

WORKDIR /flask

COPY ./src/ /flask/

COPY ./docker/flask/requirements.txt /flask/

RUN pip install --no-cache-dir -r /flask/requirements.txt

COPY ./docker/flask/.env /flask/

COPY --from=ts-build /ts/script/ /flask/static/script/

EXPOSE 5000

CMD ["python", "main.py"]
